# DrugTax: Drug taxonomy

DrugTax takes SMILES inputs and classifies the molecule according to their taxonomy, organic or inorganic kingdom and their subclasses, using a 0/1 binary classification for each one. It generates a vector of 163 features including the taxonomy classification and other key information such as number of carbons, nitrogens… These vectors can be used for subsequent molecular representation in chemoinformatic pipelines.

## Identifiers

* EOS model ID: `eos24ci`
* Slug: `drugtax`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Integer`
* Output Shape: `List`
* Interpretation: A vector of 163 points, each one corresponding to a particular taxonomic or structural molecular feature

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-022-00649-w)
* [Source Code](https://github.com/MoreiraLAB/DrugTax)
* Ersilia contributor: [Femme-js](https://github.com/Femme-js)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos24ci)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos24ci.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos24ci) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-022-00649-w) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!