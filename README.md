# ICSM Vocabularies

This repository contains the source data for [Intergovernmental Committee on Surveying and Mapping](https://icsm.gov.au/)'s vocabularies, that is managed structured lists of terms.

The vocabularies are formulated according to the [Simple Knowledge Organization System (SKOS)](https://www.w3.org/TR/skos-reference/) model and will be display online in human- and machine-readable form in Q4, 2024.

Some of the vocabularies here are in test display online at:

* [Queensland Spatial Information's Vocabs](https://vocabs.gsq.digital/v#qsi-vocabs)

## Copyright & License

These vocabularies are all $copy; ICSM, 2024, unless otherwise indicated within the vocabulary.

All content of this repository is licensed for reuse with the [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/) licence, in accordance with Australian Government open data policy.


## Contact

The following people are contacts for different aspects of this repository:

_Overall administration_  
_Land Parcel vocabularies_    
**Roger Fraser**  
Victoria Department of Transport and Planning  
<roger.fraser@transport.vic.gov.au>

_Addresses vocabularies_  
_Geographical Names vocabularies_  
_Transport Networks vocabularies_  
**Anne Goldsack**  
_Chair Addressing Working Group, ICSM_  
Queensland Spatial Information  
<anne.goldsack@resources.qld.gov.au>  


_Technical content_  
**Nicholas Car**  
<nick@kurrawong.ai>


## Prez resources

This listing of the resources in this repository is used by the [Prez System](https://kurrawong.ai/products/prez/) to display the vocabularies correctly.


| Resource             | Location                                                                                                              | Notes                                                   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Catalogue Definition | `catalogue.ttl`                                                                                                       |                                                         |
| Items                | `./vocabs/**/*.ttl`                                                                                                   | Multiple ttl files in multiple subfolders               |
| Profile Definition   | [Prez Records Profile](https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttl) | Default Prez profile for Records API                    |
| Context Resources    | `_background/*.ttl`                                                                                                   | Multiple labels files for ontologies, licenses & agents |

### Vocab testing process

1. Install packages listed in tests/requirements.txt
2. Use scripts top validate all vocabs: `pytest`
3. Use `tests/labelify_all.py` to identify any missing labels
    * add any missing to `_background`
4. Manually create/update the `cattalogue.ttl` file
