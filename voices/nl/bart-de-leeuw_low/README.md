# Dutch bart-de-leeuw (Low Quality)

A single-speaker model for Dutch based on the [CSS10 dataset](https://www.kaggle.com/bryanpark/dutch-single-speaker-speech-dataset).

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
<td> · </td>
<td> silence </td>
</tr>
<tr>
<td> 4 </td>
<td> # </td>
<td> word break </td>
</tr>
<tr>
<td> 5 </td>
<td> ˈ </td>
<td> primary stress </td>
</tr>
<tr>
<td> 6 </td>
<td> ˌ </td>
<td> secondary stress </td>
</tr>
<tr>
<td> 7 </td>
<td> a </td>
<td>  </td>
</tr>
<tr>
<td> 8 </td>
<td> aː </td>
<td>  </td>
</tr>
<tr>
<td> 9 </td>
<td> b </td>
<td>  </td>
</tr>
<tr>
<td> 10 </td>
<td> c </td>
<td>  </td>
</tr>
<tr>
<td> 11 </td>
<td> d </td>
<td>  </td>
</tr>
<tr>
<td> 12 </td>
<td> e </td>
<td>  </td>
</tr>
<tr>
<td> 13 </td>
<td> eː </td>
<td>  </td>
</tr>
<tr>
<td> 14 </td>
<td> f </td>
<td>  </td>
</tr>
<tr>
<td> 15 </td>
<td> h </td>
<td>  </td>
</tr>
<tr>
<td> 16 </td>
<td> i </td>
<td>  </td>
</tr>
<tr>
<td> 17 </td>
<td> iː </td>
<td>  </td>
</tr>
<tr>
<td> 18 </td>
<td> j </td>
<td>  </td>
</tr>
<tr>
<td> 19 </td>
<td> k </td>
<td>  </td>
</tr>
<tr>
<td> 20 </td>
<td> l </td>
<td>  </td>
</tr>
<tr>
<td> 21 </td>
<td> m </td>
<td>  </td>
</tr>
<tr>
<td> 22 </td>
<td> n </td>
<td>  </td>
</tr>
<tr>
<td> 23 </td>
<td> o </td>
<td>  </td>
</tr>
<tr>
<td> 24 </td>
<td> oː </td>
<td>  </td>
</tr>
<tr>
<td> 25 </td>
<td> p </td>
<td>  </td>
</tr>
<tr>
<td> 26 </td>
<td> s </td>
<td>  </td>
</tr>
<tr>
<td> 27 </td>
<td> t </td>
<td>  </td>
</tr>
<tr>
<td> 28 </td>
<td> u </td>
<td>  </td>
</tr>
<tr>
<td> 29 </td>
<td> uː </td>
<td>  </td>
</tr>
<tr>
<td> 30 </td>
<td> v </td>
<td>  </td>
</tr>
<tr>
<td> 31 </td>
<td> w </td>
<td>  </td>
</tr>
<tr>
<td> 32 </td>
<td> x </td>
<td>  </td>
</tr>
<tr>
<td> 33 </td>
<td> y </td>
<td>  </td>
</tr>
<tr>
<td> 34 </td>
<td> yː </td>
<td>  </td>
</tr>
<tr>
<td> 35 </td>
<td> z </td>
<td>  </td>
</tr>
<tr>
<td> 36 </td>
<td> ø </td>
<td>  </td>
</tr>
<tr>
<td> 37 </td>
<td> ŋ </td>
<td>  </td>
</tr>
<tr>
<td> 38 </td>
<td> œy </td>
<td>  </td>
</tr>
<tr>
<td> 39 </td>
<td> œː </td>
<td>  </td>
</tr>
<tr>
<td> 40 </td>
<td> ɑ </td>
<td>  </td>
</tr>
<tr>
<td> 41 </td>
<td> ɑu </td>
<td>  </td>
</tr>
<tr>
<td> 42 </td>
<td> ɑː </td>
<td>  </td>
</tr>
<tr>
<td> 43 </td>
<td> ɔ </td>
<td>  </td>
</tr>
<tr>
<td> 44 </td>
<td> ɔː </td>
<td>  </td>
</tr>
<tr>
<td> 45 </td>
<td> ə </td>
<td>  </td>
</tr>
<tr>
<td> 46 </td>
<td> ɛ </td>
<td>  </td>
</tr>
<tr>
<td> 47 </td>
<td> ɛi </td>
<td>  </td>
</tr>
<tr>
<td> 48 </td>
<td> ɛː </td>
<td>  </td>
</tr>
<tr>
<td> 49 </td>
<td> ɡ </td>
<td>  </td>
</tr>
<tr>
<td> 50 </td>
<td> ɣ </td>
<td>  </td>
</tr>
<tr>
<td> 51 </td>
<td> ɪ </td>
<td>  </td>
</tr>
<tr>
<td> 52 </td>
<td> ɱ </td>
<td>  </td>
</tr>
<tr>
<td> 53 </td>
<td> ɹ </td>
<td>  </td>
</tr>
<tr>
<td> 54 </td>
<td> ʃ </td>
<td>  </td>
</tr>
<tr>
<td> 55 </td>
<td> ʏ </td>
<td>  </td>
</tr>
<tr>
<td> 56 </td>
<td> ʏː </td>
<td>  </td>
</tr>
<tr>
<td> 57 </td>
<td> ʒ </td>
<td>  </td>
</tr>
<tr>
<td> 58 </td>
<td> ʔ </td>
<td>  </td>
</tr>
</table>
