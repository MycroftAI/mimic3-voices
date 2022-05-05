# Ukrainian M-AILabs (Low Quality)

A multi-speaker model for Ukrainian based on the [M-AILabs dataset](https://www.caito.de/2019/01/03/the-m-ailabs-speech-dataset/).

See LICENSE file for license.


## Phonemes

<table><thead><th>&nbsp;</th><th>Phoneme</th><th>Description</th></thead>
<tr>
<td> 0 </td>
<td> _ </td>
<td> padding </td>
</tr>
<tr>
<td> 1 </td>
<td> ^ </td>
<td> start utterance </td>
</tr>
<tr>
<td> 2 </td>
<td> $ </td>
<td> end utterance </td>
</tr>
<tr>
<td> 3 </td>
<td> , </td>
<td> short pause (minor break) </td>
</tr>
<tr>
<td> 4 </td>
<td> . </td>
<td> long pause (major break) </td>
</tr>
<tr>
<td> 5 </td>
<td> # </td>
<td> word break </td>
</tr>
<tr>
<td> 6 </td>
<td> ' </td>
<td> ' </td>
</tr>
<tr>
<td> 7 </td>
<td> - </td>
<td> - </td>
</tr>
<tr>
<td> 8 </td>
<td> Є </td>
<td> Є </td>
</tr>
<tr>
<td> 9 </td>
<td> І </td>
<td> І </td>
</tr>
<tr>
<td> 10 </td>
<td> Ї </td>
<td> Ї </td>
</tr>
<tr>
<td> 11 </td>
<td> А </td>
<td> А </td>
</tr>
<tr>
<td> 12 </td>
<td> Б </td>
<td> Б </td>
</tr>
<tr>
<td> 13 </td>
<td> В </td>
<td> В </td>
</tr>
<tr>
<td> 14 </td>
<td> Г </td>
<td> Г </td>
</tr>
<tr>
<td> 15 </td>
<td> Д </td>
<td> Д </td>
</tr>
<tr>
<td> 16 </td>
<td> Е </td>
<td> Е </td>
</tr>
<tr>
<td> 17 </td>
<td> Ж </td>
<td> Ж </td>
</tr>
<tr>
<td> 18 </td>
<td> З </td>
<td> З </td>
</tr>
<tr>
<td> 19 </td>
<td> И </td>
<td> И </td>
</tr>
<tr>
<td> 20 </td>
<td> Й </td>
<td> Й </td>
</tr>
<tr>
<td> 21 </td>
<td> К </td>
<td> К </td>
</tr>
<tr>
<td> 22 </td>
<td> Л </td>
<td> Л </td>
</tr>
<tr>
<td> 23 </td>
<td> М </td>
<td> М </td>
</tr>
<tr>
<td> 24 </td>
<td> Н </td>
<td> Н </td>
</tr>
<tr>
<td> 25 </td>
<td> О </td>
<td> О </td>
</tr>
<tr>
<td> 26 </td>
<td> П </td>
<td> П </td>
</tr>
<tr>
<td> 27 </td>
<td> Р </td>
<td> Р </td>
</tr>
<tr>
<td> 28 </td>
<td> С </td>
<td> С </td>
</tr>
<tr>
<td> 29 </td>
<td> Т </td>
<td> Т </td>
</tr>
<tr>
<td> 30 </td>
<td> У </td>
<td> У </td>
</tr>
<tr>
<td> 31 </td>
<td> Ф </td>
<td> Ф </td>
</tr>
<tr>
<td> 32 </td>
<td> Х </td>
<td> Х </td>
</tr>
<tr>
<td> 33 </td>
<td> Ц </td>
<td> Ц </td>
</tr>
<tr>
<td> 34 </td>
<td> Ч </td>
<td> Ч </td>
</tr>
<tr>
<td> 35 </td>
<td> Ш </td>
<td> Ш </td>
</tr>
<tr>
<td> 36 </td>
<td> Щ </td>
<td> Щ </td>
</tr>
<tr>
<td> 37 </td>
<td> Ь </td>
<td> Ь </td>
</tr>
<tr>
<td> 38 </td>
<td> Ю </td>
<td> Ю </td>
</tr>
<tr>
<td> 39 </td>
<td> Я </td>
<td> Я </td>
</tr>
<tr>
<td> 40 </td>
<td> а </td>
<td> а </td>
</tr>
<tr>
<td> 41 </td>
<td> б </td>
<td> б </td>
</tr>
<tr>
<td> 42 </td>
<td> в </td>
<td> в </td>
</tr>
<tr>
<td> 43 </td>
<td> г </td>
<td> г </td>
</tr>
<tr>
<td> 44 </td>
<td> д </td>
<td> д </td>
</tr>
<tr>
<td> 45 </td>
<td> е </td>
<td> е </td>
</tr>
<tr>
<td> 46 </td>
<td> ж </td>
<td> ж </td>
</tr>
<tr>
<td> 47 </td>
<td> з </td>
<td> з </td>
</tr>
<tr>
<td> 48 </td>
<td> и </td>
<td> и </td>
</tr>
<tr>
<td> 49 </td>
<td> й </td>
<td> й </td>
</tr>
<tr>
<td> 50 </td>
<td> к </td>
<td> к </td>
</tr>
<tr>
<td> 51 </td>
<td> л </td>
<td> л </td>
</tr>
<tr>
<td> 52 </td>
<td> м </td>
<td> м </td>
</tr>
<tr>
<td> 53 </td>
<td> н </td>
<td> н </td>
</tr>
<tr>
<td> 54 </td>
<td> о </td>
<td> о </td>
</tr>
<tr>
<td> 55 </td>
<td> п </td>
<td> п </td>
</tr>
<tr>
<td> 56 </td>
<td> р </td>
<td> р </td>
</tr>
<tr>
<td> 57 </td>
<td> с </td>
<td> с </td>
</tr>
<tr>
<td> 58 </td>
<td> т </td>
<td> т </td>
</tr>
<tr>
<td> 59 </td>
<td> у </td>
<td> у </td>
</tr>
<tr>
<td> 60 </td>
<td> ф </td>
<td> ф </td>
</tr>
<tr>
<td> 61 </td>
<td> х </td>
<td> х </td>
</tr>
<tr>
<td> 62 </td>
<td> ц </td>
<td> ц </td>
</tr>
<tr>
<td> 63 </td>
<td> ч </td>
<td> ч </td>
</tr>
<tr>
<td> 64 </td>
<td> ш </td>
<td> ш </td>
</tr>
<tr>
<td> 65 </td>
<td> щ </td>
<td> щ </td>
</tr>
<tr>
<td> 66 </td>
<td> ь </td>
<td> ь </td>
</tr>
<tr>
<td> 67 </td>
<td> ю </td>
<td> ю </td>
</tr>
<tr>
<td> 68 </td>
<td> я </td>
<td> я </td>
</tr>
<tr>
<td> 69 </td>
<td> є </td>
<td> є </td>
</tr>
<tr>
<td> 70 </td>
<td> і </td>
<td> і </td>
</tr>
<tr>
<td> 71 </td>
<td> ї </td>
<td> ї </td>
</tr>
<tr>
<td> 72 </td>
<td> Ґ </td>
<td> Ґ </td>
</tr>
<tr>
<td> 73 </td>
<td> ґ </td>
<td> ґ </td>
</tr>
</table>
