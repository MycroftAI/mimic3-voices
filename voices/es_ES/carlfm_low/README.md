# Spanish carlfm (Low Quality)

A single-speaker model for Spanish based on the [Carlos Fonseca's 100h dataset](https://github.com/carlfm01/my-speech-datasets).

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
<td> ai </td>
<td> dipthong </td>
</tr>
<tr>
<td> 9 </td>
<td> au </td>
<td> dipthong </td>
</tr>
<tr>
<td> 10 </td>
<td> b </td>
<td> consonant plosive bilabial voiced [<a title="Audio sample for consonant plosive bilabial voiced " href="../../../phonemes/voiced_bilabial_plosive.wav">Sample</a>] </td>
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
<td> ei </td>
<td> dipthong </td>
</tr>
<tr>
<td> 14 </td>
<td> eu </td>
<td> dipthong </td>
</tr>
<tr>
<td> 15 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced [<a title="Audio sample for consonant fricative labio-dental unvoiced " href="../../../phonemes/voiceless_labiodental_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 16 </td>
<td> g </td>
<td> consonant plosive velar voiced [<a title="Audio sample for consonant plosive velar voiced " href="../../../phonemes/voiced_velar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 17 </td>
<td> i </td>
<td> vowel close front unrounded [<a title="Audio sample for vowel close front unrounded " href="../../../phonemes/close_front_unrounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 18 </td>
<td> k </td>
<td> consonant plosive velar unvoiced [<a title="Audio sample for consonant plosive velar unvoiced " href="../../../phonemes/voiceless_velar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 19 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced [<a title="Audio sample for consonant lateral-approximant alveolar voiced " href="../../../phonemes/alveolar_lateral_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 20 </td>
<td> m </td>
<td> consonant nasal bilabial voiced [<a title="Audio sample for consonant nasal bilabial voiced " href="../../../phonemes/bilabial_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 21 </td>
<td> n </td>
<td> consonant nasal alveolar voiced [<a title="Audio sample for consonant nasal alveolar voiced " href="../../../phonemes/alveolar_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 22 </td>
<td> o </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 23 </td>
<td> oi </td>
<td> dipthong </td>
</tr>
<tr>
<td> 24 </td>
<td> ou </td>
<td> dipthong </td>
</tr>
<tr>
<td> 25 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced [<a title="Audio sample for consonant plosive bilabial unvoiced " href="../../../phonemes/voiceless_bilabial_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 26 </td>
<td> r </td>
<td> consonant trill alveolar voiced [<a title="Audio sample for consonant trill alveolar voiced " href="../../../phonemes/alveolar_trill.wav">Sample</a>] </td>
</tr>
<tr>
<td> 27 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced [<a title="Audio sample for consonant fricative alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 28 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced [<a title="Audio sample for consonant plosive alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_plosive.wav">Sample</a>] </td>
</tr>
<tr>
<td> 29 </td>
<td> t͡ʃ </td>
<td> consonant affricate post-alveolar unvoiced [<a title="Audio sample for consonant affricate post-alveolar unvoiced " href="../../../phonemes/voiceless_postalveolar_affricate.wav">Sample</a>] </td>
</tr>
<tr>
<td> 30 </td>
<td> u </td>
<td> vowel close back rounded [<a title="Audio sample for vowel close back rounded " href="../../../phonemes/close_back_rounded_vowel.wav">Sample</a>] </td>
</tr>
<tr>
<td> 31 </td>
<td> wa </td>
<td>  </td>
</tr>
<tr>
<td> 32 </td>
<td> we </td>
<td>  </td>
</tr>
<tr>
<td> 33 </td>
<td> wi </td>
<td>  </td>
</tr>
<tr>
<td> 34 </td>
<td> wo </td>
<td>  </td>
</tr>
<tr>
<td> 35 </td>
<td> x </td>
<td> consonant fricative velar unvoiced [<a title="Audio sample for consonant fricative velar unvoiced " href="../../../phonemes/voiceless_velar_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 36 </td>
<td> ɲ </td>
<td> consonant nasal palatal voiced [<a title="Audio sample for consonant nasal palatal voiced " href="../../../phonemes/palatal_nasal.wav">Sample</a>] </td>
</tr>
<tr>
<td> 37 </td>
<td> ɾ </td>
<td> consonant flap alveolar voiced </td>
</tr>
<tr>
<td> 38 </td>
<td> ʎ </td>
<td> consonant lateral-approximant palatal voiced [<a title="Audio sample for consonant lateral-approximant palatal voiced " href="../../../phonemes/palatal_lateral_approximant.wav">Sample</a>] </td>
</tr>
<tr>
<td> 39 </td>
<td> ʝ </td>
<td> consonant fricative palatal unvoiced [<a title="Audio sample for consonant fricative palatal unvoiced " href="../../../phonemes/voiceless_palatal_fricative.wav">Sample</a>] </td>
</tr>
<tr>
<td> 40 </td>
<td> θ </td>
<td> consonant fricative dental unvoiced [<a title="Audio sample for consonant fricative dental unvoiced " href="../../../phonemes/voiceless_dental_fricative.wav">Sample</a>] </td>
</tr>
</table>
