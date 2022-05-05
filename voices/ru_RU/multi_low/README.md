# Russian multi (Low Quality)

A multi-speaker model for Russian based on:

* [CSS10](https://www.kaggle.com/bryanpark/russian-single-speaker-speech-dataset)
* [M-AILabs](https://www.caito.de/2019/01/03/the-m-ailabs-speech-dataset/)

See LICENSE files for licenses.


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
<td> vowel open front unrounded<br /><audio controls preload="none" src="phonemes/open_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 8 </td>
<td> aː </td>
<td> vowel open front unrounded<br /><audio controls preload="none" src="phonemes/open_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 9 </td>
<td> b </td>
<td> consonant plosive bilabial voiced<br /><audio controls preload="none" src="phonemes/voiced_bilabial_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 10 </td>
<td> bʲ </td>
<td>  </td>
</tr>
<tr>
<td> 11 </td>
<td> d </td>
<td> consonant plosive alveolar voiced<br /><audio controls preload="none" src="phonemes/voiced_alveolar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 12 </td>
<td> dʲ </td>
<td>  </td>
</tr>
<tr>
<td> 13 </td>
<td> e </td>
<td> vowel close-mid front unrounded<br /><audio controls preload="none" src="phonemes/close-mid_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 14 </td>
<td> eː </td>
<td> vowel close-mid front unrounded<br /><audio controls preload="none" src="phonemes/close-mid_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 15 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_labiodental_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 16 </td>
<td> fʲ </td>
<td>  </td>
</tr>
<tr>
<td> 17 </td>
<td> i </td>
<td> vowel close front unrounded<br /><audio controls preload="none" src="phonemes/close_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 18 </td>
<td> iː </td>
<td> vowel close front unrounded<br /><audio controls preload="none" src="phonemes/close_front_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 19 </td>
<td> j </td>
<td> consonant approximant palatal voiced<br /><audio controls preload="none" src="phonemes/palatal_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 20 </td>
<td> k </td>
<td> consonant plosive velar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_velar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 21 </td>
<td> kʲ </td>
<td>  </td>
</tr>
<tr>
<td> 22 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_lateral_approximant.wav"></audio> </td>
</tr>
<tr>
<td> 23 </td>
<td> lʲ </td>
<td>  </td>
</tr>
<tr>
<td> 24 </td>
<td> m </td>
<td> consonant nasal bilabial voiced<br /><audio controls preload="none" src="phonemes/bilabial_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 25 </td>
<td> mʲ </td>
<td>  </td>
</tr>
<tr>
<td> 26 </td>
<td> n </td>
<td> consonant nasal alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_nasal.wav"></audio> </td>
</tr>
<tr>
<td> 27 </td>
<td> nʲ </td>
<td>  </td>
</tr>
<tr>
<td> 28 </td>
<td> o </td>
<td> vowel close-mid back rounded<br /><audio controls preload="none" src="phonemes/close-mid_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 29 </td>
<td> oː </td>
<td> vowel close-mid back rounded<br /><audio controls preload="none" src="phonemes/close-mid_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 30 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_bilabial_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 31 </td>
<td> pʲ </td>
<td>  </td>
</tr>
<tr>
<td> 32 </td>
<td> r </td>
<td> consonant trill alveolar voiced<br /><audio controls preload="none" src="phonemes/alveolar_trill.wav"></audio> </td>
</tr>
<tr>
<td> 33 </td>
<td> rʲ </td>
<td>  </td>
</tr>
<tr>
<td> 34 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_alveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 35 </td>
<td> sʲ </td>
<td>  </td>
</tr>
<tr>
<td> 36 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_alveolar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 37 </td>
<td> tʲ </td>
<td>  </td>
</tr>
<tr>
<td> 38 </td>
<td> t͡s </td>
<td> consonant affricate alveolar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_alveolar_affricate.wav"></audio> </td>
</tr>
<tr>
<td> 39 </td>
<td> t͡ɕ </td>
<td> consonant affricate palatal unvoiced </td>
</tr>
<tr>
<td> 40 </td>
<td> u </td>
<td> vowel close back rounded<br /><audio controls preload="none" src="phonemes/close_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 41 </td>
<td> uː </td>
<td> vowel close back rounded<br /><audio controls preload="none" src="phonemes/close_back_rounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 42 </td>
<td> v </td>
<td> consonant fricative labio-dental voiced<br /><audio controls preload="none" src="phonemes/voiced_labiodental_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 43 </td>
<td> vʲ </td>
<td>  </td>
</tr>
<tr>
<td> 44 </td>
<td> x </td>
<td> consonant fricative velar unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_velar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 45 </td>
<td> xʲ </td>
<td>  </td>
</tr>
<tr>
<td> 46 </td>
<td> z </td>
<td> consonant fricative alveolar voiced<br /><audio controls preload="none" src="phonemes/voiced_alveolar_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 47 </td>
<td> zʲ </td>
<td>  </td>
</tr>
<tr>
<td> 48 </td>
<td> ɕː </td>
<td>  </td>
</tr>
<tr>
<td> 49 </td>
<td> ɡ </td>
<td> consonant plosive velar voiced<br /><audio controls preload="none" src="phonemes/voiced_velar_plosive.wav"></audio> </td>
</tr>
<tr>
<td> 50 </td>
<td> ɡʲ </td>
<td>  </td>
</tr>
<tr>
<td> 51 </td>
<td> ɨ </td>
<td> vowel close central unrounded<br /><audio controls preload="none" src="phonemes/close_central_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 52 </td>
<td> ɨː </td>
<td> vowel close central unrounded<br /><audio controls preload="none" src="phonemes/close_central_unrounded_vowel.wav"></audio> </td>
</tr>
<tr>
<td> 53 </td>
<td> ʂ </td>
<td> consonant fricative retroflex unvoiced<br /><audio controls preload="none" src="phonemes/voiceless_retroflex_fricative.wav"></audio> </td>
</tr>
<tr>
<td> 54 </td>
<td> ʐ </td>
<td> consonant fricative palatal voiced<br /><audio controls preload="none" src="phonemes/voiced_palatal_fricative.wav"></audio> </td>
</tr>
</table>
