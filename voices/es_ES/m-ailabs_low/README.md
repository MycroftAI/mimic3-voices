# Spanish M-AILabs (Low Quality)

A multi-speaker model for Spanish based on the [M-AILabs dataset](https://www.caito.de/2019/01/03/the-m-ailabs-speech-dataset/).

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
<td> ˈ </td>
<td> primary stress </td>
</tr>
<tr>
<td> 7 </td>
<td> ˌ </td>
<td> secondary stress </td>
</tr>
<tr>
<td> 8 </td>
<td> a </td>
<td> vowel open front unrounded<br /><audio controls preload="none" src="phonemes/open_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 9 </td>
<td> aɪ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 10 </td>
<td> aʊ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 11 </td>
<td> b </td>
<td> consonant plosive bilabial voiced<br /><audio controls preload="none" src="phonemes/voiced_bilabial_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 12 </td>
<td> d </td>
<td> consonant plosive alveolar voiced<br /><audio controls preload="none" src="phonemes/voiced_alveolar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 13 </td>
<td> dʒ </td>
<td>  </td>
</tr>
<tr>
<td> 14 </td>
<td> e </td>
<td> vowel close-mid front unrounded<br /><audio controls preload="none" src="phonemes/close-mid_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 15 </td>
<td> eɪ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 16 </td>
<td> eʊ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 17 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_labiodental_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 18 </td>
<td> i </td>
<td> vowel close front unrounded<br /><audio controls preload="none" src="phonemes/close_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 19 </td>
<td> iː </td>
<td> vowel close front unrounded<br /><audio controls preload="none" src="phonemes/close_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 20 </td>
<td> j </td>
<td> consonant approximant palatal voiced<br /><audio controls preload="none" src="phonemes/palatal_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 21 </td>
<td> k </td>
<td> consonant plosive velar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_velar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 22 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_lateral_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 23 </td>
<td> m </td>
<td> consonant nasal bilabial voiced<br /><audio controls preload="none" src="phonemes/bilabial_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 24 </td>
<td> n </td>
<td> consonant nasal alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 25 </td>
<td> o </td>
<td> vowel close-mid back rounded<br /><audio controls preload="none" src="phonemes/close-mid_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 26 </td>
<td> oɪ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 27 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_bilabial_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 28 </td>
<td> pː </td>
<td> consonant plosive bilabial unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_bilabial_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 29 </td>
<td> r </td>
<td> consonant trill alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_trill.wav"></audio> </td>
</tr>
<tr>
<td> 30 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_alveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 31 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_alveolar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 32 </td>
<td> ts </td>
<td>  </td>
</tr>
<tr>
<td> 33 </td>
<td> tʃ </td>
<td>  </td>
</tr>
<tr>
<td> 34 </td>
<td> u </td>
<td> vowel close back rounded<br /><audio controls preload="none" src="phonemes/close_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 35 </td>
<td> w </td>
<td> consonant approximant bilabial voiced<br /><audio controls preload="none" src="phonemes/voiced_bilabial_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 36 </td>
<td> x </td>
<td> consonant fricative velar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_velar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 37 </td>
<td> ð </td>
<td> consonant fricative dental voiced<br /><audio controls preload="none" src="phonemes/voiced_dental_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 38 </td>
<td> ŋ </td>
<td> consonant nasal velar voiced<br /><audio controls preload="none" src="phonemes/velar_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 39 </td>
<td> ɛ </td>
<td> vowel open-mid front unrounded<br /><audio controls preload="none" src="phonemes/open-mid_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 40 </td>
<td> ɟ </td>
<td> consonant plosive palatal voiced<br /><audio controls preload="none" src="phonemes/voiced_palatal_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 41 </td>
<td> ɡ </td>
<td> consonant plosive velar voiced<br /><audio controls preload="none" src="phonemes/voiced_velar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 42 </td>
<td> ɣ </td>
<td> consonant fricative velar voiced<br /><audio controls preload="none" src="phonemes/voiced_velar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 43 </td>
<td> ɲ </td>
<td> consonant nasal palatal voiced<br /><audio controls preload="none" src="phonemes/palatal_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 44 </td>
<td> ɾ </td>
<td> consonant flap alveolar voiced </td>
</tr>
<tr>
<td> 45 </td>
<td> ʃ </td>
<td> consonant fricative post-alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_postalveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 46 </td>
<td> ʎ </td>
<td> consonant lateral-approximant palatal voiced<br /><audio controls preload="none" src="phonemes/palatal_lateral_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 47 </td>
<td> ʝ </td>
<td> consonant fricative palatal unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_palatal_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 48 </td>
<td> β </td>
<td> consonant fricative bilabial voiced<br /><audio controls preload="none" src="phonemes/voiced_bilabial_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 49 </td>
<td> θ </td>
<td> consonant fricative dental unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_dental_fricative.wav"></audio> </td>
</tr>
</table>
