package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
)

// ASSUMPTIONS:
// - each line of the input file contains the same number of fields, thus separator symbols
// - portions of text wrapped in quotation marks and brakets are considered as such
//   that do not contain the separator inside
// - only punctuation and space related symbols are considered as valid separators,
// 	 alphanumerical separators are not allowed
// - only double quote `"` is considered as a valid quotation mark

// NbLn is a number of lines to be read in the beggining of the input file
// 20 is big enough to be confident that there is no multiple characters competing for the "Delimeter status"
var NbLn int = 20

func main() {
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

	// get rid of text
	// remove letters, digits, math symbols, currency signs, dingbats, box-drawing characters, etc
	// reg, err := regexp.Compile("[\\pL\\pN\\pS]")
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// for i, v := range fstNLines {
	// 	fstNLines[i] = reg.ReplaceAllString(v, "")
	// }

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
		// fmt.Println(fstNLines)
		punctuation = append(punctuation, reg.FindAllString(v, -1))
	}
	fmt.Println(punctuation)

	// count character frequencies
	var charCountPerLine []map[string]int
	lineCountPerChar := make(map[string]int)
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

	fmt.Println(lineCountPerChar)
	potentSep := make(map[string]int)
	for char := range lineCountPerChar {

		if lineCountPerChar[char] == len(fstNLines) {
			// fmt.Println("lineCountPerChar[char] == len(fstNLines)")
			potentSep[char] = 0
		}
	}

	fmt.Println("--------------")

	for _, line := range charCountPerLine {
		fmt.Println(line, potentSep)
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
	fmt.Println("--------------")
	fmt.Println(potentSep)

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
