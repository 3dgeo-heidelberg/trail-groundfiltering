# Welcome to the TRAIL Workshop on Archaeological Ground Point Filtering of LiDAR Point Clouds!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

An important task in the processing of airborne laser scanning data is the derivation of appropriate models (terrain, surface, feature). Setting up such classification and filtering workflows can be time-consuming and prone to information loss, especially in geographically heterogeneous landscapes. AFwizard is an open source Python package designed to improve the productivity of ground point filtering workflows in archaeology and beyond. It provides a Jupyter-based environment for human-in-the-loop, spatially heterogeneous ground point filtering. Through hands-on training, the participants will learn how to study the effects of different algorithm and parameter combinations on digital terrain modelling in a practical and time-saving way. In addition, the AFwizard settings will be tested and analysed using simulated lidar survey scenarios (e.g., airborne, UAV, terrestrial) and point densities. In order to learn how different point cloud properties affect the filtering process, the open source simulator HELIOS++ will be introduced and used together with AFwizard in a hands-on exercise. This will allow for improved filtering of existing data as well as future survey planning.

## What to expect

- **Session 1**: Introduction to LiDAR ground point filtering using the [AFwizard](https://github.com/ssciwr/afwizard) (Adaptive Filtering Wizard)
- **Session 2**: Introduction to [HELIOS++](https://github.com/3dgeo-heidelberg/helios) (Heidelberg LiDAR Operations Simulator) and hands-on exercise to find ground point filtering pipelines for different simulated LiDAR scenarios
- **Session 3**: Application of the learned skills to further datasets (can be your own datasets, provided data or simulated data)

## Installation of necessary software

Tutorials for the installation of necessary software is documented on the [Installation page](installation.md).

## Datasets

*URLs to datasets will follow*

## Literature and References

<details>
<summary>Journal papers and conferences</summary>
<br>
Doneus, M., Höfle, B., Kempf, D., Daskalakis, G. & Shinoto, M. (2022): Human-in-the-loop development of spatially adaptive ground point filtering pipelines — An archaeological case study. Archaeological Prospection. Vol. 29 (4), pp. 503-524. <a href="https://doi.org/10.1002/arp.1873">https://doi.org/10.1002/arp.1873</a>.

```bibtex
@article{Doneus_2022,
  author  = {Michael Doneus and Bernhard H\"ofle and Dominic Kempf and Gwydion Daskalakis and Maria Shinoto},
  title   = {Human-in-the-loop development of spatially adaptive ground point filtering pipelines {\textemdash} An archaeological case study},
  journal = {Archaeological Prospection},
  year    = {2022},
  volume  = {29},
  number  = {4},
  pages   = {503--524},
  doi     = {10.1002/arp.1873},
  url     = {https://doi.org/10.1002/arp.1873}
  }
```

Winiwarter, L., Esmorís Pena, A.M., Weiser, H., Anders, K., Martínez Sánchez, J., Searle, M. & Höfle, B. (2022): Virtual laser scanning with HELIOS++: A novel take on ray tracing-based simulation of topographic full-waveform 3D laser scanning. Remote Sensing of Environment. Vol. 269, pp. 112772. <a href="https://doi.org/10.1016/j.rse.2021.112772">https://doi.org/10.1016/j.rse.2021.112772</a>.

```bibtex
@article{heliosPlusPlus,
  author = {Lukas Winiwarter and Alberto Manuel {Esmorís Pena} and Hannah Weiser and Katharina Anders and Jorge {Martínez Sánchez} and Mark Searle and Bernhard Höfle},
  title = {Virtual laser scanning with HELIOS++: A novel take on ray tracing-based   simulation of topographic full-waveform 3D laser scanning},
  journal = {Remote Sensing of Environment},
  year = {2022},
  volume = {269},
  issn = {0034-4257},
  doi = {https://doi.org/10.1016/j.rse.2021.112772},
  keywords = {Software, LiDAR simulation, Point cloud, Data generation, Voxel, Vegetation modelling, Diffuse media}
} 
```

</details>

<details>
<summary>Software</summary>

<ul>
<li><a href="https://github.com/3dgeo-heidelberg/helios">HELIOS++</a></li>
<li><a href="https://github.com/3dgeo-heidelberg/helios/wiki">HELIOS++ Wiki</a></li>
<li><a href="https://github.com/ssciwr/afwizard">AFwizard</a></li>
<li><a href="https://afwizard.readthedocs.io/en/latest/">AFwizard documentation</a></li>
<li><a href="https://rapidlasso.de/">LAStools</a></li>
<li><a href="https://jupyter.org/">Jupyter</a></li>
</ul>

</details>


## Acknowledgements

This workshop is part of the [TRAIL](https://trail.zrc-sazu.si/) Meeting 2025 under the theme "Airborne laser scanning for farmed landscapes". TRAIL (Training and Research in the Archaeological Interpretation of Lidar) was founded to provide opportunities to share expertise and provide training in the archaeological use of LiDAR.

The sixth TRAIL Meeting is organized by [ZRC SAZU](https://www.zrc-sazu.si/en) (Slovenia) in partnership with [Historic Environment Scotland](https://www.historicenvironment.scot/) (United Kingdom), [CNRS](https://www.cnrs.fr/en) (France), [University of Clermont Auvergne](https://www.uca.fr/en) (France), CLUE+, [Vrije Universiteit Amsterdam](https://vu.nl/nl) (The Netherlands), and [University of Amsterdam](https://www.uva.nl/en) (the Netherlands). It is financially supported by [ZRC SAZU](https://www.zrc-sazu.si/en), [Historic Environment Scotland](https://www.historicenvironment.scot/), [Aerial Archaeology Research Group](https://aargonline.com/wp/), [Slovenian Research and Innovation Agency](https://www.aris-rs.si/en/) (programme P2-0406) and [European Research Council](https://erc.europa.eu/) (project [STONE](https://cordis.europa.eu/project/id/101089123), GAP-101089123).

<table>
  <tr>
    <td style="color:black; padding:10px;">
      <img src="img/logotipi-TRAIL-VI-1.png?raw=true" alt="Organisers and financers of the sixth TRAIL Meeting"/><br/>
      Organisers and financers of the sixth TRAIL Meeting.
    </td>
  </tr>
</table>

The workshop was prepared by [Michael Doneus](https://uha.univie.ac.at/ueber-uns/personen/wissenschaftliche-mitarbeiterinnen/universitaetsprofessorinnen/michael-doneus-institutsvorstand/) (Professor of landscape archaeology, University of Vienna), [Hannah Weiser](https://www.geog.uni-heidelberg.de/en/people-at-the-institute/hannah-weiser) ([3DGeo Research Group, Heidelberg University](https://www.uni-heidelberg.de/3dgeo)) and [Zoran Čučković](https://www.zoran-cuckovic.from.hr/). 

<center>
<table>
  <tr>
    <td style="background-color:#ffffff; color:black; padding:2px;">
      <img src="img/UniWien_CMYK_A4.svg?raw=true" alt="3DGeo Logo" width=400/><br/>
    </td>
    <td style="background-color:#ffffff; color:black; padding:2px;">
      <img src="img/3DGeo_Logo_300dpi.png?raw=true" alt="3DGeo Logo" width=400/><br/>
    </td>
  </tr>
</table>
</center>

**AFwizard** was developed by the [Scientific Software Center (SSC)](https://www.ssc.uni-heidelberg.de/en) of Heidelberg University in the framework of the project [Human-in-the-Loop Adaptive Terrain Filtering of 3D Point Clouds for Archaeological Prospection](https://ucrisportal.univie.ac.at/de/publications/human-in-the-loop-development-of-spatially-adaptive-ground-point-) led by Maria Shinoto. The Scientific Software is funded as part of the [Excellence Strategy of the German Federal and State Governments](https://www.exzellenzstrategie.de/en/).

<center>
<table>
  <tr>
    <td style="color:black; padding:2px;">
      <img src="img/ssc.png?raw=true" alt="SSC Logo" width=400/><br/>
    </td>
  </tr>
</table>
</center>

Development of **HELIOS++** is led by the [3DGeo Research Group](https://www.uni-heidelberg.de/3dgeo) and the [Scientific Software Center (SSC)](https://www.ssc.uni-heidelberg.de/en) of Heidelberg University with contributions from several collaborators. HELIOS++ is funded by the [German Research Foundation (DFG)](https://www.dfg.de/en/) in the frame of the Software projects [Fostering a community-driven and sustainable HELIOS++ scientific software](https://www.geog.uni-heidelberg.de/en/3dgeo/projects-of-the-3dgeo-research-group/fostering-a-community-driven-and-sustainable-helios-scientific-software) (528521476) and [VirtuaLearn3D](https://www.geog.uni-heidelberg.de/en/institute/geoinformatics/3dgeo-research-group/projects-of-the-3dgeo-research-group/virtualearn3d) (496418931).

<table>
  <tr>
    <td style="background-color:#ffffff; color:black; padding:2px;">
      <img src="img/logo_sustainable_helios.png?raw=true" alt="Trier Map"/><br/>
    </td>
  </tr>
</table>