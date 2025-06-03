# DrugTax: Drug taxonomy

DrugTax takes SMILES inputs and classifies the molecule according to their taxonomy, organic or inorganic kingdom and their subclasses, using a 0/1 binary classification for each one. It generates a vector of 163 features including the taxonomy classification and other key information such as number of carbons, nitrogens… These vectors can be used for subsequent molecular representation in chemoinformatic pipelines.

This model was incorporated on 2022-12-20.

## Information
### Identifiers
- **Ersilia Identifier:** `eos24ci`
- **Slug:** `drugtax`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Fingerprint`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `163`
- **Output Consistency:** `Fixed`
- **Interpretation:** A vector of 163 points, each one corresponding to a particular taxonomic or structural molecular feature

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| organic | integer |  | The molecule is an organic (1) molecule or not (0) |
| inorganic | integer |  | The molecule is an inorganic (1) molecule or not (0) |
| organoheterocyclic | integer |  | The molecule contains a organoheterocyclic group (1) or not (0) |
| benzenoid | integer |  | The molecule contains a benzenoid group (1) or not (0) |
| organosulfur | integer |  | The molecule contains a organosulfur group (1) or not (0) |
| lipid | integer |  | The molecule contains a lipid group (1) or not (0) |
| allene | integer |  | The molecule contains a allene group (1) or not (0) |
| phenylpropanoids_and_polyketides | integer |  | The molecule contains a phenylpropanoids_and_polyketides group (1) or not (0) |
| carboxyl | integer |  | The molecule contains a carboxyl group (1) or not (0) |
| organic_acid | integer |  | The molecule contains a organic_acid group (1) or not (0) |

_10 of 163 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos24ci](https://hub.docker.com/r/ersiliaos/eos24ci)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos24ci.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos24ci.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `700`
- **Image Size (Mb):** `647.82`

**Computational Performance (seconds):**
- 10 inputs: `29.88`
- 100 inputs: `21.32`
- 10000 inputs: `312.35`

### References
- **Source Code**: [https://github.com/MoreiraLAB/DrugTax](https://github.com/MoreiraLAB/DrugTax)
- **Publication**: [https://jcheminf.biomedcentral.com/articles/10.1186/s13321-022-00649-w](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-022-00649-w)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [Femme-js](https://github.com/Femme-js)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos24ci
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos24ci
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
