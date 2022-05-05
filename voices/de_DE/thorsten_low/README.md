# German thorsten (Low Quality)

A single-speaker model for German based on the [Thorsten dataset](https://github.com/thorstenMueller/deep-learning-german-tts/).

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
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 8 </td>
<td> aɪ̯ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 9 </td>
<td> aʊ̯ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 10 </td>
<td> aː </td>
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 11 </td>
<td> b </td>
<td> consonant plosive bilabial voiced [<a title="Audio sample for consonant plosive bilabial voiced " href="../../../phonemes/voiced_bilabial_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 12 </td>
<td> d </td>
<td> consonant plosive alveolar voiced [<a title="Audio sample for consonant plosive alveolar voiced " href="../../../phonemes/voiced_alveolar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 13 </td>
<td> eː </td>
<td> vowel close-mid front unrounded [<a title="Audio sample for vowel close-mid front unrounded " href="../../../phonemes/close-mid_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 14 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced [<a title="Audio sample for consonant fricative labio-dental unvoiced " href="../../../phonemes/voiceless_labiodental_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 15 </td>
<td> g </td>
<td> consonant plosive velar voiced [<a title="Audio sample for consonant plosive velar voiced " href="../../../phonemes/voiced_velar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 16 </td>
<td> h </td>
<td> consonant fricative glottal unvoiced [<a title="Audio sample for consonant fricative glottal unvoiced " href="../../../phonemes/voiceless_glottal_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 17 </td>
<td> iː </td>
<td> vowel close front unrounded [<a title="Audio sample for vowel close front unrounded " href="../../../phonemes/close_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 18 </td>
<td> j </td>
<td> consonant approximant palatal voiced [<a title="Audio sample for consonant approximant palatal voiced " href="../../../phonemes/palatal_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 19 </td>
<td> k </td>
<td> consonant plosive velar unvoiced [<a title="Audio sample for consonant plosive velar unvoiced " href="../../../phonemes/voiceless_velar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 20 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced [<a title="Audio sample for consonant lateral-approximant alveolar voiced " href="../../../phonemes/alveolar_lateral_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 21 </td>
<td> m </td>
<td> consonant nasal bilabial voiced [<a title="Audio sample for consonant nasal bilabial voiced " href="../../../phonemes/bilabial_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 22 </td>
<td> n </td>
<td> consonant nasal alveolar voiced [<a title="Audio sample for consonant nasal alveolar voiced " href="../../../phonemes/alveolar_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 23 </td>
<td> oː </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 24 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced [<a title="Audio sample for consonant plosive bilabial unvoiced " href="../../../phonemes/voiceless_bilabial_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 25 </td>
<td> p͡f </td>
<td> consonant affricate labio-dental unvoiced </td>
</tr>
<tr>
<td> 26 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced [<a title="Audio sample for consonant fricative alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 27 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced [<a title="Audio sample for consonant plosive alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 28 </td>
<td> t͡s </td>
<td> consonant affricate alveolar unvoiced [<a title="Audio sample for consonant affricate alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_affricate.wav">Sample</a>] </td>
</tr>
<tr>
<td> 29 </td>
<td> t͡ʃ </td>
<td> consonant affricate post-alveolar unvoiced [<a title="Audio sample for consonant affricate post-alveolar unvoiced " href="../../../phonemes/voiceless_postalveolar_affricate.wav">Sample</a>] </td>
</tr>
<tr>
<td> 30 </td>
<td> uː </td>
<td> vowel close back rounded [<a title="Audio sample for vowel close back rounded " href="../../../phonemes/close_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 31 </td>
<td> v </td>
<td> consonant fricative labio-dental voiced [<a title="Audio sample for consonant fricative labio-dental voiced " href="../../../phonemes/voiced_labiodental_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 32 </td>
<td> x </td>
<td> consonant fricative velar unvoiced [<a title="Audio sample for consonant fricative velar unvoiced " href="../../../phonemes/voiceless_velar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 33 </td>
<td> yː </td>
<td> vowel close front rounded [<a title="Audio sample for vowel close front rounded " href="../../../phonemes/close_front_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 34 </td>
<td> z </td>
<td> consonant fricative alveolar voiced [<a title="Audio sample for consonant fricative alveolar voiced " href="../../../phonemes/voiced_alveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 35 </td>
<td> ãː </td>
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 36 </td>
<td> ç </td>
<td> consonant fricative palatal unvoiced [<a title="Audio sample for consonant fricative palatal unvoiced " href="../../../phonemes/voiceless_palatal_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 37 </td>
<td> õː </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 38 </td>
<td> øː </td>
<td> vowel close-mid front rounded [<a title="Audio sample for vowel close-mid front rounded " href="../../../phonemes/close-mid_front_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 39 </td>
<td> ŋ </td>
<td> consonant nasal velar voiced [<a title="Audio sample for consonant nasal velar voiced " href="../../../phonemes/velar_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 40 </td>
<td> œ </td>
<td> vowel open-mid front rounded [<a title="Audio sample for vowel open-mid front rounded " href="../../../phonemes/open-mid_front_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 41 </td>
<td> ɐ </td>
<td> vowel near-open central unrounded [<a title="Audio sample for vowel near-open central unrounded " href="../../../phonemes/near-open_central_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 42 </td>
<td> ɔ </td>
<td> vowel open-mid back rounded [<a title="Audio sample for vowel open-mid back rounded " href="../../../phonemes/open-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 43 </td>
<td> ɔʏ̯ </td>
<td> dipthong </td>
</tr>
<tr>
<td> 44 </td>
<td> ə </td>
<td> vowel mid central unrounded </td>
</tr>
<tr>
<td> 45 </td>
<td> ɛ </td>
<td> vowel open-mid front unrounded [<a title="Audio sample for vowel open-mid front unrounded " href="../../../phonemes/open-mid_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 46 </td>
<td> ɛː </td>
<td> vowel open-mid front unrounded [<a title="Audio sample for vowel open-mid front unrounded " href="../../../phonemes/open-mid_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 47 </td>
<td> ɛ̃ː </td>
<td> vowel open-mid front unrounded [<a title="Audio sample for vowel open-mid front unrounded " href="../../../phonemes/open-mid_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 48 </td>
<td> ɪ </td>
<td> vowel near-close near-front unrounded [<a title="Audio sample for vowel near-close near-front unrounded " href="../../../phonemes/near-close_near-front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 49 </td>
<td> ʁ </td>
<td> consonant fricative uvular voiced [<a title="Audio sample for consonant fricative uvular voiced " href="../../../phonemes/voiced_uvular_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 50 </td>
<td> ʃ </td>
<td> consonant fricative post-alveolar unvoiced [<a title="Audio sample for consonant fricative post-alveolar unvoiced " href="../../../phonemes/voiceless_postalveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 51 </td>
<td> ʊ </td>
<td> vowel near-close near-back rounded [<a title="Audio sample for vowel near-close near-back rounded " href="../../../phonemes/near-close_near-back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 52 </td>
<td> ʏ </td>
<td> vowel near-close near-front rounded [<a title="Audio sample for vowel near-close near-front rounded " href="../../../phonemes/near-close_near-front_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 53 </td>
<td> ʒ </td>
<td> consonant fricative post-alveolar voiced [<a title="Audio sample for consonant fricative post-alveolar voiced " href="../../../phonemes/voiced_postalveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 54 </td>
<td> ʔ </td>
<td> consonant plosive glottal unvoiced [<a title="Audio sample for consonant plosive glottal unvoiced " href="../../../phonemes/glottal_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 55 </td>
<td> χ </td>
<td> consonant fricative uvular unvoiced [<a title="Audio sample for consonant fricative uvular unvoiced " href="../../../phonemes/voiceless_uvular_fricative.wav">Sample</a>] </td>
</tr>
</table>
