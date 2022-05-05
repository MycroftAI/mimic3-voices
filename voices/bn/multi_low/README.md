# Bengali multi (Low Quality)

A multi-speaker model for Bengali based on:

* [cmu-indic](http://festvox.org/cmu_indic/)
* [google](http://www.openslr.org/37/)

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
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 9 </td>
<td> b </td>
<td> consonant plosive bilabial voiced [<a title="Audio sample for consonant plosive bilabial voiced " href="../../../phonemes/voiced_bilabial_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 10 </td>
<td> c </td>
<td> consonant plosive palatal unvoiced [<a title="Audio sample for consonant plosive palatal unvoiced " href="../../../phonemes/voiceless_palatal_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 11 </td>
<td> d </td>
<td> consonant plosive alveolar voiced [<a title="Audio sample for consonant plosive alveolar voiced " href="../../../phonemes/voiced_alveolar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 12 </td>
<td> e </td>
<td> vowel close-mid front unrounded [<a title="Audio sample for vowel close-mid front unrounded " href="../../../phonemes/close-mid_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 13 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced [<a title="Audio sample for consonant fricative labio-dental unvoiced " href="../../../phonemes/voiceless_labiodental_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 14 </td>
<td> h </td>
<td> consonant fricative glottal unvoiced [<a title="Audio sample for consonant fricative glottal unvoiced " href="../../../phonemes/voiceless_glottal_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 15 </td>
<td> i </td>
<td> vowel close front unrounded [<a title="Audio sample for vowel close front unrounded " href="../../../phonemes/close_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 16 </td>
<td> j </td>
<td> consonant approximant palatal voiced [<a title="Audio sample for consonant approximant palatal voiced " href="../../../phonemes/palatal_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 17 </td>
<td> k </td>
<td> consonant plosive velar unvoiced [<a title="Audio sample for consonant plosive velar unvoiced " href="../../../phonemes/voiceless_velar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 18 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced [<a title="Audio sample for consonant lateral-approximant alveolar voiced " href="../../../phonemes/alveolar_lateral_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 19 </td>
<td> m </td>
<td> consonant nasal bilabial voiced [<a title="Audio sample for consonant nasal bilabial voiced " href="../../../phonemes/bilabial_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 20 </td>
<td> n </td>
<td> consonant nasal alveolar voiced [<a title="Audio sample for consonant nasal alveolar voiced " href="../../../phonemes/alveolar_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 21 </td>
<td> o </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 22 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced [<a title="Audio sample for consonant plosive bilabial unvoiced " href="../../../phonemes/voiceless_bilabial_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 23 </td>
<td> p̃ </td>
<td> consonant plosive bilabial unvoiced [<a title="Audio sample for consonant plosive bilabial unvoiced " href="../../../phonemes/voiceless_bilabial_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 24 </td>
<td> r </td>
<td> consonant trill alveolar voiced [<a title="Audio sample for consonant trill alveolar voiced " href="../../../phonemes/alveolar_trill.wav">Sample</a>] </td>
</tr>
<tr>
<td> 25 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced [<a title="Audio sample for consonant fricative alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 26 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced [<a title="Audio sample for consonant plosive alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 27 </td>
<td> u </td>
<td> vowel close back rounded [<a title="Audio sample for vowel close back rounded " href="../../../phonemes/close_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 28 </td>
<td> v </td>
<td> consonant fricative labio-dental voiced [<a title="Audio sample for consonant fricative labio-dental voiced " href="../../../phonemes/voiced_labiodental_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 29 </td>
<td> w </td>
<td> consonant approximant bilabial voiced [<a title="Audio sample for consonant approximant bilabial voiced " href="../../../phonemes/voiced_bilabial_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 30 </td>
<td> ã </td>
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 31 </td>
<td> æ </td>
<td> vowel near-open front unrounded [<a title="Audio sample for vowel near-open front unrounded " href="../../../phonemes/near-open_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 32 </td>
<td> õ </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 33 </td>
<td> ĩ </td>
<td> vowel close front unrounded [<a title="Audio sample for vowel close front unrounded " href="../../../phonemes/close_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 34 </td>
<td> ŋ </td>
<td> consonant nasal velar voiced [<a title="Audio sample for consonant nasal velar voiced " href="../../../phonemes/velar_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 35 </td>
<td> ũ </td>
<td> vowel close back rounded [<a title="Audio sample for vowel close back rounded " href="../../../phonemes/close_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 36 </td>
<td> ɐ </td>
<td> vowel near-open central unrounded [<a title="Audio sample for vowel near-open central unrounded " href="../../../phonemes/near-open_central_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 37 </td>
<td> ɑ </td>
<td> vowel open back unrounded [<a title="Audio sample for vowel open back unrounded " href="../../../phonemes/open_back_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 38 </td>
<td> ɒ </td>
<td> vowel open back rounded [<a title="Audio sample for vowel open back rounded " href="../../../phonemes/open_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 39 </td>
<td> ɔ </td>
<td> vowel open-mid back rounded [<a title="Audio sample for vowel open-mid back rounded " href="../../../phonemes/open-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 40 </td>
<td> ɔ̃ </td>
<td> vowel open-mid back rounded [<a title="Audio sample for vowel open-mid back rounded " href="../../../phonemes/open-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 41 </td>
<td> ɖ </td>
<td> consonant plosive retroflex voiced [<a title="Audio sample for consonant plosive retroflex voiced " href="../../../phonemes/voiced_retroflex_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 42 </td>
<td> ə </td>
<td> vowel mid central unrounded </td>
</tr>
<tr>
<td> 43 </td>
<td> ɛ </td>
<td> vowel open-mid front unrounded [<a title="Audio sample for vowel open-mid front unrounded " href="../../../phonemes/open-mid_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 44 </td>
<td> ɜ </td>
<td> vowel open-mid central unrounded [<a title="Audio sample for vowel open-mid central unrounded " href="../../../phonemes/open-mid_central_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 45 </td>
<td> ɟ </td>
<td> consonant plosive palatal voiced [<a title="Audio sample for consonant plosive palatal voiced " href="../../../phonemes/voiced_palatal_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 46 </td>
<td> ɡ </td>
<td> consonant plosive velar voiced [<a title="Audio sample for consonant plosive velar voiced " href="../../../phonemes/voiced_velar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 47 </td>
<td> ɪ </td>
<td> vowel near-close near-front unrounded [<a title="Audio sample for vowel near-close near-front unrounded " href="../../../phonemes/near-close_near-front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 48 </td>
<td> ɹ </td>
<td> consonant approximant alveolar voiced [<a title="Audio sample for consonant approximant alveolar voiced " href="../../../phonemes/alveolar_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 49 </td>
<td> ɾ </td>
<td> consonant flap alveolar voiced </td>
</tr>
<tr>
<td> 50 </td>
<td> ʃ </td>
<td> consonant fricative post-alveolar unvoiced [<a title="Audio sample for consonant fricative post-alveolar unvoiced " href="../../../phonemes/voiceless_postalveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 51 </td>
<td> ʈ </td>
<td> consonant plosive retroflex unvoiced [<a title="Audio sample for consonant plosive retroflex unvoiced " href="../../../phonemes/voiceless_retroflex_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 52 </td>
<td> ʊ </td>
<td> vowel near-close near-back rounded [<a title="Audio sample for vowel near-close near-back rounded " href="../../../phonemes/near-close_near-back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 53 </td>
<td> ʒ </td>
<td> consonant fricative post-alveolar voiced [<a title="Audio sample for consonant fricative post-alveolar voiced " href="../../../phonemes/voiced_postalveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 54 </td>
<td> ʰ </td>
<td>  </td>
</tr>
<tr>
<td> 55 </td>
<td> ː </td>
<td> elongation </td>
</tr>
<tr>
<td> 56 </td>
<td> ẽ </td>
<td> vowel close-mid front unrounded [<a title="Audio sample for vowel close-mid front unrounded " href="../../../phonemes/close-mid_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
</table>
