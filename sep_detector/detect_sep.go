package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
)

// ASSUMPTIONS:
// - each line of the input file contains the same number of fields, thus the same number of separator symbols
// - portions of text wrapped in quotation marks and brakets are considered as such
//   that do not contain the separator inside
// - only punctuation symbols and tabs are considered as valid separators,
// 	 alphanumerical separators are not allowed
// - only double quote `"` is considered as a valid quotation mark

// NbLn is a number of lines to be read in the beggining of the input file
// 20 is big enough to be confident that there is no multiple characters competing for the "Delimeter status"
var NbLn int = 20

func main() {
	// read input file
	srcName := os.Args[1]
	file, err := os.Open(srcName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var fstNLines []string

	n := 0
	for scanner.Scan() {
		n++
		line := scanner.Text()
		fstNLines = append(fstNLines, line)
		if n == NbLn {
			break
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// remove text in quotes and brakets
	regQuote := regexp.MustCompile(`"[^"\r\n]*"`)
	regBraket1 := regexp.MustCompile(`\([^\r\n]*\)`)
	regBraket2 := regexp.MustCompile(`\[[^\r\n]*\]`)
	regBraket3 := regexp.MustCompile(`\{[^\r\n]*\}`)

	for i := range fstNLines {
		fstNLines[i] = regQuote.ReplaceAllString(fstNLines[i], "")
		fstNLines[i] = regBraket1.ReplaceAllString(fstNLines[i], "")
		fstNLines[i] = regBraket2.ReplaceAllString(fstNLines[i], "")
		fstNLines[i] = regBraket3.ReplaceAllString(fstNLines[i], "")
	}

	// find punctuation
	var punctuation [][]string
	reg := regexp.MustCompile("[\t!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]")
	for _, v := range fstNLines {
		punctuation = append(punctuation, reg.FindAllString(v, -1))
	}

	// count character frequencies
	var charCountPerLine []map[string]int    // nb of char occurences in each line
	lineCountPerChar := make(map[string]int) // nb of char occurences across all the lines
	for _, chars := range punctuation {
		charCount := make(map[string]int)
		for _, v := range chars {
			charCount[v]++
		}
		for v := range charCount {
			lineCountPerChar[v]++
		}
		charCountPerLine = append(charCountPerLine, charCount)
	}

	potentSep := make(map[string]int)
	for char := range lineCountPerChar {
		if lineCountPerChar[char] == len(fstNLines) {
			potentSep[char] = 0
		}
	}

	for _, line := range charCountPerLine {
		for char := range line {
			_, present := potentSep[char]
			if present {
				if potentSep[char] == 0 {
					potentSep[char] = line[char]
				} else if potentSep[char] != line[char] {
					delete(potentSep, char)
				}
			}
		}
	}

	var fileSep string
	for char := range potentSep {
		if fileSep == "" {
			fileSep = char
		} else if potentSep[char] > potentSep[fileSep] {
			fileSep = char
		}
	}

	fmt.Printf("The input file has `%s` as a separator.\n", fileSep)

}
