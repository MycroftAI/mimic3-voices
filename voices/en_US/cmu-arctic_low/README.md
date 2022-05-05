# U.S English CMU Arctic (Low Quality)

A multi-speaker model for U.S. English based on the [CMU Arctic dataset](http://www.festvox.org/cmu_arctic/).

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
<td> aɪ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 8 </td>
<td> aʊ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 9 </td>
<td> b </td>
<td> consonant plosive bilabial voiced<br /><audio controls preload="none" src="phonemes/voiced_bilabial_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 10 </td>
<td> d </td>
<td> consonant plosive alveolar voiced<br /><audio controls preload="none" src="phonemes/voiced_alveolar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 11 </td>
<td> d͡ʒ </td>
<td> consonant affricate post-alveolar voiced<br /><audio controls preload="none" src="phonemes/voiced_postalveolar_affricate.wav"></audio> </td>
</tr>
<tr>
<td> 12 </td>
<td> eɪ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 13 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_labiodental_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 14 </td>
<td> h </td>
<td> consonant fricative glottal unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_glottal_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 15 </td>
<td> i </td>
<td> vowel close front unrounded<br /><audio controls preload="none" src="phonemes/close_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 16 </td>
<td> j </td>
<td> consonant approximant palatal voiced<br /><audio controls preload="none" src="phonemes/palatal_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 17 </td>
<td> k </td>
<td> consonant plosive velar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_velar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 18 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_lateral_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 19 </td>
<td> m </td>
<td> consonant nasal bilabial voiced<br /><audio controls preload="none" src="phonemes/bilabial_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 20 </td>
<td> n </td>
<td> consonant nasal alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 21 </td>
<td> oʊ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 22 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_bilabial_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 23 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_alveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 24 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_alveolar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 25 </td>
<td> t͡ʃ </td>
<td> consonant affricate post-alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_postalveolar_affricate.wav"></audio> </td>
</tr>
<tr>
<td> 26 </td>
<td> u </td>
<td> vowel close back rounded<br /><audio controls preload="none" src="phonemes/close_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 27 </td>
<td> v </td>
<td> consonant fricative labio-dental voiced<br /><audio controls preload="none" src="phonemes/voiced_labiodental_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 28 </td>
<td> w </td>
<td> consonant approximant bilabial voiced<br /><audio controls preload="none" src="phonemes/voiced_bilabial_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 29 </td>
<td> z </td>
<td> consonant fricative alveolar voiced<br /><audio controls preload="none" src="phonemes/voiced_alveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 30 </td>
<td> æ </td>
<td> vowel near-open front unrounded<br /><audio controls preload="none" src="phonemes/near-open_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 31 </td>
<td> ð </td>
<td> consonant fricative dental voiced<br /><audio controls preload="none" src="phonemes/voiced_dental_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 32 </td>
<td> ŋ </td>
<td> consonant nasal velar voiced<br /><audio controls preload="none" src="phonemes/velar_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 33 </td>
<td> ɑ </td>
<td> vowel open back unrounded<br /><audio controls preload="none" src="phonemes/open_back_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 34 </td>
<td> ɔ </td>
<td> vowel open-mid back rounded<br /><audio controls preload="none" src="phonemes/open-mid_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 35 </td>
<td> ɔɪ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 36 </td>
<td> ə </td>
<td> vowel mid central unrounded </td>
</tr>
<tr>
<td> 37 </td>
<td> ɚ </td>
<td> schwa r-coloured<br /><audio controls preload="none" src="phonemes/alveolar_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 38 </td>
<td> ɛ </td>
<td> vowel open-mid front unrounded<br /><audio controls preload="none" src="phonemes/open-mid_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 39 </td>
<td> ɡ </td>
<td> consonant plosive velar voiced<br /><audio controls preload="none" src="phonemes/voiced_velar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 40 </td>
<td> ɪ </td>
<td> vowel near-close near-front unrounded<br /><audio controls preload="none" src="phonemes/near-close_near-front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 41 </td>
<td> ɹ </td>
<td> consonant approximant alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 42 </td>
<td> ʃ </td>
<td> consonant fricative post-alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_postalveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 43 </td>
<td> ʊ </td>
<td> vowel near-close near-back rounded<br /><audio controls preload="none" src="phonemes/near-close_near-back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 44 </td>
<td> ʌ </td>
<td> vowel open-mid back unrounded<br /><audio controls preload="none" src="phonemes/open-mid_back_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 45 </td>
<td> ʒ </td>
<td> consonant fricative post-alveolar voiced<br /><audio controls preload="none" src="phonemes/voiced_postalveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 46 </td>
<td> θ </td>
<td> consonant fricative dental unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_dental_fricative.wav"></audio> </td>
</tr>
</table>
