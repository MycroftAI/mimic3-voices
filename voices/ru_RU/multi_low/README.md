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
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 8 </td>
<td> aː </td>
<td> vowel open front unrounded [<a title="Audio sample for vowel open front unrounded " href="../../../phonemes/open_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 9 </td>
<td> b </td>
<td> consonant plosive bilabial voiced [<a title="Audio sample for consonant plosive bilabial voiced " href="../../../phonemes/voiced_bilabial_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 10 </td>
<td> bʲ </td>
<td>  </td>
</tr>
<tr>
<td> 11 </td>
<td> d </td>
<td> consonant plosive alveolar voiced [<a title="Audio sample for consonant plosive alveolar voiced " href="../../../phonemes/voiced_alveolar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 12 </td>
<td> dʲ </td>
<td>  </td>
</tr>
<tr>
<td> 13 </td>
<td> e </td>
<td> vowel close-mid front unrounded [<a title="Audio sample for vowel close-mid front unrounded " href="../../../phonemes/close-mid_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 14 </td>
<td> eː </td>
<td> vowel close-mid front unrounded [<a title="Audio sample for vowel close-mid front unrounded " href="../../../phonemes/close-mid_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 15 </td>
<td> f </td>
<td> consonant fricative labio-dental unvoiced [<a title="Audio sample for consonant fricative labio-dental unvoiced " href="../../../phonemes/voiceless_labiodental_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 16 </td>
<td> fʲ </td>
<td>  </td>
</tr>
<tr>
<td> 17 </td>
<td> i </td>
<td> vowel close front unrounded [<a title="Audio sample for vowel close front unrounded " href="../../../phonemes/close_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 18 </td>
<td> iː </td>
<td> vowel close front unrounded [<a title="Audio sample for vowel close front unrounded " href="../../../phonemes/close_front_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 19 </td>
<td> j </td>
<td> consonant approximant palatal voiced [<a title="Audio sample for consonant approximant palatal voiced " href="../../../phonemes/palatal_approximant.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 20 </td>
<td> k </td>
<td> consonant plosive velar unvoiced [<a title="Audio sample for consonant plosive velar unvoiced " href="../../../phonemes/voiceless_velar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 21 </td>
<td> kʲ </td>
<td>  </td>
</tr>
<tr>
<td> 22 </td>
<td> l </td>
<td> consonant lateral-approximant alveolar voiced [<a title="Audio sample for consonant lateral-approximant alveolar voiced " href="../../../phonemes/alveolar_lateral_approximant.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 23 </td>
<td> lʲ </td>
<td>  </td>
</tr>
<tr>
<td> 24 </td>
<td> m </td>
<td> consonant nasal bilabial voiced [<a title="Audio sample for consonant nasal bilabial voiced " href="../../../phonemes/bilabial_nasal.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 25 </td>
<td> mʲ </td>
<td>  </td>
</tr>
<tr>
<td> 26 </td>
<td> n </td>
<td> consonant nasal alveolar voiced [<a title="Audio sample for consonant nasal alveolar voiced " href="../../../phonemes/alveolar_nasal.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 27 </td>
<td> nʲ </td>
<td>  </td>
</tr>
<tr>
<td> 28 </td>
<td> o </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 29 </td>
<td> oː </td>
<td> vowel close-mid back rounded [<a title="Audio sample for vowel close-mid back rounded " href="../../../phonemes/close-mid_back_rounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 30 </td>
<td> p </td>
<td> consonant plosive bilabial unvoiced [<a title="Audio sample for consonant plosive bilabial unvoiced " href="../../../phonemes/voiceless_bilabial_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 31 </td>
<td> pʲ </td>
<td>  </td>
</tr>
<tr>
<td> 32 </td>
<td> r </td>
<td> consonant trill alveolar voiced [<a title="Audio sample for consonant trill alveolar voiced " href="../../../phonemes/alveolar_trill.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 33 </td>
<td> rʲ </td>
<td>  </td>
</tr>
<tr>
<td> 34 </td>
<td> s </td>
<td> consonant fricative alveolar unvoiced [<a title="Audio sample for consonant fricative alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 35 </td>
<td> sʲ </td>
<td>  </td>
</tr>
<tr>
<td> 36 </td>
<td> t </td>
<td> consonant plosive alveolar unvoiced [<a title="Audio sample for consonant plosive alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 37 </td>
<td> tʲ </td>
<td>  </td>
</tr>
<tr>
<td> 38 </td>
<td> t͡s </td>
<td> consonant affricate alveolar unvoiced [<a title="Audio sample for consonant affricate alveolar unvoiced " href="../../../phonemes/voiceless_alveolar_affricate.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 39 </td>
<td> t͡ɕ </td>
<td> consonant affricate palatal unvoiced </td>
</tr>
<tr>
<td> 40 </td>
<td> u </td>
<td> vowel close back rounded [<a title="Audio sample for vowel close back rounded " href="../../../phonemes/close_back_rounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 41 </td>
<td> uː </td>
<td> vowel close back rounded [<a title="Audio sample for vowel close back rounded " href="../../../phonemes/close_back_rounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 42 </td>
<td> v </td>
<td> consonant fricative labio-dental voiced [<a title="Audio sample for consonant fricative labio-dental voiced " href="../../../phonemes/voiced_labiodental_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 43 </td>
<td> vʲ </td>
<td>  </td>
</tr>
<tr>
<td> 44 </td>
<td> x </td>
<td> consonant fricative velar unvoiced [<a title="Audio sample for consonant fricative velar unvoiced " href="../../../phonemes/voiceless_velar_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 45 </td>
<td> xʲ </td>
<td>  </td>
</tr>
<tr>
<td> 46 </td>
<td> z </td>
<td> consonant fricative alveolar voiced [<a title="Audio sample for consonant fricative alveolar voiced " href="../../../phonemes/voiced_alveolar_fricative.wav?raw=true">Sample</a>] </td>
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
<td> consonant plosive velar voiced [<a title="Audio sample for consonant plosive velar voiced " href="../../../phonemes/voiced_velar_plosive.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 50 </td>
<td> ɡʲ </td>
<td>  </td>
</tr>
<tr>
<td> 51 </td>
<td> ɨ </td>
<td> vowel close central unrounded [<a title="Audio sample for vowel close central unrounded " href="../../../phonemes/close_central_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 52 </td>
<td> ɨː </td>
<td> vowel close central unrounded [<a title="Audio sample for vowel close central unrounded " href="../../../phonemes/close_central_unrounded_vowel.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 53 </td>
<td> ʂ </td>
<td> consonant fricative retroflex unvoiced [<a title="Audio sample for consonant fricative retroflex unvoiced " href="../../../phonemes/voiceless_retroflex_fricative.wav?raw=true">Sample</a>] </td>
</tr>
<tr>
<td> 54 </td>
<td> ʐ </td>
<td> consonant fricative palatal voiced [<a title="Audio sample for consonant fricative palatal voiced " href="../../../phonemes/voiced_palatal_fricative.wav?raw=true">Sample</a>] </td>
</tr>
</table>
