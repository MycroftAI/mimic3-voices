# Korean KSS (Low Quality)

A single-speaker model for KSS based on the [CSS10 dataset](https://www.kaggle.com/bryanpark/korean-single-speaker-speech-dataset).

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
<td> | </td>
<td> short pause (minor break) </td>
</tr>
<tr>
<td> 4 </td>
<td> ‖ </td>
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
<td> , </td>
<td> short pause (minor break) </td>
</tr>
<tr>
<td> 9 </td>
<td> - </td>
<td>  </td>
</tr>
<tr>
<td> 10 </td>
<td> . </td>
<td> long pause (major break) </td>
</tr>
<tr>
<td> 11 </td>
<td> a </td>
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 12 </td>
<td> b </td>
<td> consonant plosive bilabial voiced [<a title="Audio sample for consonant plosive bilabial voiced " href="../../../phonemes/voiced_bilabial_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 13 </td>
<td> d </td>
<td> consonant plosive alveolar voiced [<a title="Audio sample for consonant plosive alveolar voiced " href="../../../phonemes/voiced_alveolar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 14 </td>
<td> e </td>
<td> vowel close-mid front unrounded [<a title="Audio sample for vowel close-mid front unrounded " href="../../../phonemes/close-mid_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 15 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced [<a title="Audio sample for consonant fricative labio-dental unvoiced " href="../../../phonemes/voiceless_labiodental_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 16 </td>
<td> h </td>
<td> consonant fricative glottal unvoiced [<a title="Audio sample for consonant fricative glottal unvoiced " href="../../../phonemes/voiceless_glottal_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 17 </td>
<td> i </td>
<td> vowel close front unrounded [<a title="Audio sample for vowel close front unrounded " href="../../../phonemes/close_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 18 </td>
<td> j </td>
<td> consonant approximant palatal voiced [<a title="Audio sample for consonant approximant palatal voiced " href="../../../phonemes/palatal_approximant.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 19 </td>
<td> k </td>
<td> consonant plosive velar unvoiced [<a title="Audio sample for consonant plosive velar unvoiced " href="../../../phonemes/voiceless_velar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 20 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced [<a title="Audio sample for consonant lateral-approximant alveolar voiced " href="../../../phonemes/alveolar_lateral_approximant.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 21 </td>
<td> m </td>
<td> consonant nasal bilabial voiced [<a title="Audio sample for consonant nasal bilabial voiced " href="../../../phonemes/bilabial_nasal.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 22 </td>
<td> n </td>
<td> consonant nasal alveolar voiced [<a title="Audio sample for consonant nasal alveolar voiced " href="../../../phonemes/alveolar_nasal.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 23 </td>
<td> o </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 24 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced [<a title="Audio sample for consonant plosive bilabial unvoiced " href="../../../phonemes/voiceless_bilabial_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 25 </td>
<td> q </td>
<td> consonant plosive uvular unvoiced [<a title="Audio sample for consonant plosive uvular unvoiced " href="../../../phonemes/voiceless_uvular_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 26 </td>
<td> r </td>
<td> consonant trill alveolar voiced [<a title="Audio sample for consonant trill alveolar voiced " href="../../../phonemes/alveolar_trill.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 27 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced [<a title="Audio sample for consonant fricative alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 28 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced [<a title="Audio sample for consonant plosive alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 29 </td>
<td> u </td>
<td> vowel close back rounded [<a title="Audio sample for vowel close back rounded " href="../../../phonemes/close_back_rounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 30 </td>
<td> v </td>
<td> consonant fricative labio-dental voiced [<a title="Audio sample for consonant fricative labio-dental voiced " href="../../../phonemes/voiced_labiodental_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 31 </td>
<td> w </td>
<td> consonant approximant bilabial voiced [<a title="Audio sample for consonant approximant bilabial voiced " href="../../../phonemes/voiced_bilabial_approximant.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 32 </td>
<td> ŋ </td>
<td> consonant nasal velar voiced [<a title="Audio sample for consonant nasal velar voiced " href="../../../phonemes/velar_nasal.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 33 </td>
<td> ɐ </td>
<td> vowel near-open central unrounded [<a title="Audio sample for vowel near-open central unrounded " href="../../../phonemes/near-open_central_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 34 </td>
<td> ɕ </td>
<td>  </td>
</tr>
<tr>
<td> 35 </td>
<td> ə </td>
<td> vowel mid central unrounded </td>
</tr>
<tr>
<td> 36 </td>
<td> ɛ </td>
<td> vowel open-mid front unrounded [<a title="Audio sample for vowel open-mid front unrounded " href="../../../phonemes/open-mid_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 37 </td>
<td> ɡ </td>
<td> consonant plosive velar voiced [<a title="Audio sample for consonant plosive velar voiced " href="../../../phonemes/voiced_velar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 38 </td>
<td> ɪ </td>
<td> vowel near-close near-front unrounded [<a title="Audio sample for vowel near-close near-front unrounded " href="../../../phonemes/near-close_near-front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 39 </td>
<td> ɫ </td>
<td> consonant lateral-approximant alveolar voiced [<a title="Audio sample for consonant lateral-approximant alveolar voiced " href="../../../phonemes/alveolar_lateral_approximant.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 40 </td>
<td> ɯ </td>
<td> vowel close back unrounded [<a title="Audio sample for vowel close back unrounded " href="../../../phonemes/close_back_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 41 </td>
<td> ɾ </td>
<td> consonant flap alveolar voiced </td>
</tr>
<tr>
<td> 42 </td>
<td> ʃ </td>
<td> consonant fricative post-alveolar unvoiced [<a title="Audio sample for consonant fricative post-alveolar unvoiced " href="../../../phonemes/voiceless_postalveolar_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 43 </td>
<td> ʊ </td>
<td> vowel near-close near-back rounded [<a title="Audio sample for vowel near-close near-back rounded " href="../../../phonemes/near-close_near-back_rounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 44 </td>
<td> ʌ </td>
<td> vowel open-mid back unrounded [<a title="Audio sample for vowel open-mid back unrounded " href="../../../phonemes/open-mid_back_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 45 </td>
<td> ʑ </td>
<td>  </td>
</tr>
<tr>
<td> 46 </td>
<td> ʒ </td>
<td> consonant fricative post-alveolar voiced [<a title="Audio sample for consonant fricative post-alveolar voiced " href="../../../phonemes/voiced_postalveolar_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 47 </td>
<td> ʲ </td>
<td>  </td>
</tr>
<tr>
<td> 48 </td>
<td> ː </td>
<td> elongation </td>
</tr>
</table>
