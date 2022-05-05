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
<td>  </td>
</tr>
<tr>
<td> 7 </td>
<td> - </td>
<td>  </td>
</tr>
<tr>
<td> 8 </td>
<td> Є </td>
<td>  </td>
</tr>
<tr>
<td> 9 </td>
<td> І </td>
<td>  </td>
</tr>
<tr>
<td> 10 </td>
<td> Ї </td>
<td>  </td>
</tr>
<tr>
<td> 11 </td>
<td> А </td>
<td>  </td>
</tr>
<tr>
<td> 12 </td>
<td> Б </td>
<td>  </td>
</tr>
<tr>
<td> 13 </td>
<td> В </td>
<td>  </td>
</tr>
<tr>
<td> 14 </td>
<td> Г </td>
<td>  </td>
</tr>
<tr>
<td> 15 </td>
<td> Д </td>
<td>  </td>
</tr>
<tr>
<td> 16 </td>
<td> Е </td>
<td>  </td>
</tr>
<tr>
<td> 17 </td>
<td> Ж </td>
<td>  </td>
</tr>
<tr>
<td> 18 </td>
<td> З </td>
<td>  </td>
</tr>
<tr>
<td> 19 </td>
<td> И </td>
<td>  </td>
</tr>
<tr>
<td> 20 </td>
<td> Й </td>
<td>  </td>
</tr>
<tr>
<td> 21 </td>
<td> К </td>
<td>  </td>
</tr>
<tr>
<td> 22 </td>
<td> Л </td>
<td>  </td>
</tr>
<tr>
<td> 23 </td>
<td> М </td>
<td>  </td>
</tr>
<tr>
<td> 24 </td>
<td> Н </td>
<td>  </td>
</tr>
<tr>
<td> 25 </td>
<td> О </td>
<td>  </td>
</tr>
<tr>
<td> 26 </td>
<td> П </td>
<td>  </td>
</tr>
<tr>
<td> 27 </td>
<td> Р </td>
<td>  </td>
</tr>
<tr>
<td> 28 </td>
<td> С </td>
<td>  </td>
</tr>
<tr>
<td> 29 </td>
<td> Т </td>
<td>  </td>
</tr>
<tr>
<td> 30 </td>
<td> У </td>
<td>  </td>
</tr>
<tr>
<td> 31 </td>
<td> Ф </td>
<td>  </td>
</tr>
<tr>
<td> 32 </td>
<td> Х </td>
<td>  </td>
</tr>
<tr>
<td> 33 </td>
<td> Ц </td>
<td>  </td>
</tr>
<tr>
<td> 34 </td>
<td> Ч </td>
<td>  </td>
</tr>
<tr>
<td> 35 </td>
<td> Ш </td>
<td>  </td>
</tr>
<tr>
<td> 36 </td>
<td> Щ </td>
<td>  </td>
</tr>
<tr>
<td> 37 </td>
<td> Ь </td>
<td>  </td>
</tr>
<tr>
<td> 38 </td>
<td> Ю </td>
<td>  </td>
</tr>
<tr>
<td> 39 </td>
<td> Я </td>
<td>  </td>
</tr>
<tr>
<td> 40 </td>
<td> а </td>
<td>  </td>
</tr>
<tr>
<td> 41 </td>
<td> б </td>
<td>  </td>
</tr>
<tr>
<td> 42 </td>
<td> в </td>
<td>  </td>
</tr>
<tr>
<td> 43 </td>
<td> г </td>
<td>  </td>
</tr>
<tr>
<td> 44 </td>
<td> д </td>
<td>  </td>
</tr>
<tr>
<td> 45 </td>
<td> е </td>
<td>  </td>
</tr>
<tr>
<td> 46 </td>
<td> ж </td>
<td>  </td>
</tr>
<tr>
<td> 47 </td>
<td> з </td>
<td>  </td>
</tr>
<tr>
<td> 48 </td>
<td> и </td>
<td>  </td>
</tr>
<tr>
<td> 49 </td>
<td> й </td>
<td>  </td>
</tr>
<tr>
<td> 50 </td>
<td> к </td>
<td>  </td>
</tr>
<tr>
<td> 51 </td>
<td> л </td>
<td>  </td>
</tr>
<tr>
<td> 52 </td>
<td> м </td>
<td>  </td>
</tr>
<tr>
<td> 53 </td>
<td> н </td>
<td>  </td>
</tr>
<tr>
<td> 54 </td>
<td> о </td>
<td>  </td>
</tr>
<tr>
<td> 55 </td>
<td> п </td>
<td>  </td>
</tr>
<tr>
<td> 56 </td>
<td> р </td>
<td>  </td>
</tr>
<tr>
<td> 57 </td>
<td> с </td>
<td>  </td>
</tr>
<tr>
<td> 58 </td>
<td> т </td>
<td>  </td>
</tr>
<tr>
<td> 59 </td>
<td> у </td>
<td>  </td>
</tr>
<tr>
<td> 60 </td>
<td> ф </td>
<td>  </td>
</tr>
<tr>
<td> 61 </td>
<td> х </td>
<td>  </td>
</tr>
<tr>
<td> 62 </td>
<td> ц </td>
<td>  </td>
</tr>
<tr>
<td> 63 </td>
<td> ч </td>
<td>  </td>
</tr>
<tr>
<td> 64 </td>
<td> ш </td>
<td>  </td>
</tr>
<tr>
<td> 65 </td>
<td> щ </td>
<td>  </td>
</tr>
<tr>
<td> 66 </td>
<td> ь </td>
<td>  </td>
</tr>
<tr>
<td> 67 </td>
<td> ю </td>
<td>  </td>
</tr>
<tr>
<td> 68 </td>
<td> я </td>
<td>  </td>
</tr>
<tr>
<td> 69 </td>
<td> є </td>
<td>  </td>
</tr>
<tr>
<td> 70 </td>
<td> і </td>
<td>  </td>
</tr>
<tr>
<td> 71 </td>
<td> ї </td>
<td>  </td>
</tr>
<tr>
<td> 72 </td>
<td> Ґ </td>
<td>  </td>
</tr>
<tr>
<td> 73 </td>
<td> ґ </td>
<td>  </td>
</tr>
</table>
