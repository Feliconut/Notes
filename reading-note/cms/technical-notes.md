# Apr 8 2025 - Directory and File structure for Root files

## File location, naming conventions

The data is from: `/eos/purdue/store/user/jduarteq/2016postVFP/spinCorrInput_2016postVFP_January2023/Nominal/ee/ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_2.root`

`eos`: This is a file system used at CERN and other institutions for storing large datasets. It is designed to handle high-throughput data access and is often used in high-energy physics experiments.
The `eos` server is mounted to our local system, so we can access it as if it were a local directory.

`eos/purdue/`: This is the directory where we have read-only access to.

`user/juarteq/`: Juan's personal storage directory. 

`2016postVFP/`: This is the `era` of the data. The possible eras include:
- `2016preVFP`
- `2016postVFP`
- `2017`
- `2018`

`spinCorrInput_2016postVFP_January2023/`: This is the `dataset` name. The dataset name is usually a combination of the era and the type of data. In this example, Juan has only imported the spinCorrInput data from the original source (which I'm currently not concerned about.)

`Nominal/`: This is the `systematic` name. `Nominal` corresponds to the plain case without any systematic variations. In our example, the other possible values are:

```bash
cd spinCorrInput_2016postVFP_January2023/
ls
AMCATNLOFXFX             JESFlavorPureBottom_DOWN  JESPileUpPtBB_UP        JESRelativePtBB_DOWN     JESSinglePionHCAL_UP
ELE_SCALESMEARING_DOWN   JESFlavorPureBottom_UP    JESPileUpPtEC1_DOWN     JESRelativePtBB_UP       JESTimePtEta_DOWN
ELE_SCALESMEARING_UP     JESFlavorPureCharm_DOWN   JESPileUpPtEC1_UP       JESRelativePtEC1_DOWN    JESTimePtEta_UP
ELE_SCALE_STAT_DOWN      JESFlavorPureCharm_UP     JESPileUpPtEC2_DOWN     JESRelativePtEC1_UP      JES_UP
ELE_SCALE_STAT_UP        JESFlavorPureGluon_DOWN   JESPileUpPtEC2_UP       JESRelativePtEC2_DOWN    MADGRAPHMLM
ERDON                    JESFlavorPureGluon_UP     JESPileUpPtHF_DOWN      JESRelativePtEC2_UP      MASS_DOWN
ERDONRETUNE              JESFlavorPureQuark_DOWN   JESPileUpPtHF_UP        JESRelativePtHF_DOWN     MASS_UP
GLUONMOVETUNE            JESFlavorPureQuark_UP     JESPileUpPtRef_DOWN     JESRelativePtHF_UP       MATCH_DOWN
JER_DOWN                 JESFlavorQCD_DOWN         JESPileUpPtRef_UP       JESRelativeSample_DOWN   MATCH_UP
JER_UP                   JESFlavorQCD_UP           JESRelativeBal_DOWN     JESRelativeSample_UP     MUON_SCALE_DOWN
JESAbsoluteMPFBias_DOWN  JESFlavorRealistic_DOWN   JESRelativeBal_UP       JESRelativeStatEC_DOWN   MUON_SCALE_UP
JESAbsoluteMPFBias_UP    JESFlavorRealistic_UP     JESRelativeFSR_DOWN     JESRelativeStatEC_UP     Nominal
JESAbsoluteScale_DOWN    JESFlavorZJet_DOWN        JESRelativeFSR_UP       JESRelativeStatFSR_DOWN  POWHEGV2HERWIG
JESAbsoluteScale_UP      JESFlavorZJet_UP          JESRelativeJEREC1_DOWN  JESRelativeStatFSR_UP    UETUNE_DOWN
JESAbsoluteStat_DOWN     JESFragmentation_DOWN     JESRelativeJEREC1_UP    JESRelativeStatHF_DOWN   UETUNE_UP
JESAbsoluteStat_UP       JESFragmentation_UP       JESRelativeJEREC2_DOWN  JESRelativeStatHF_UP     UNCLUSTERED_DOWN
JES_DOWN                 JESPileUpDataMC_DOWN      JESRelativeJEREC2_UP    JESSinglePionECAL_DOWN   UNCLUSTERED_UP
JESFlavorPhotonJet_DOWN  JESPileUpDataMC_UP        JESRelativeJERHF_DOWN   JESSinglePionECAL_UP
JESFlavorPhotonJet_UP    JESPileUpPtBB_DOWN        JESRelativeJERHF_UP     JESSinglePionHCAL_DOWN
```

Need to ask Juan what those are. Are they mentioned in Jason's analysis note?

`ee/`: This is the `channel` name. The possible channels are:
- `ee`
- `emu`
- `mumu`

`ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_2.root`: This is a single root file. In this example, it contains the data for `step0` and `step8`, with kinematics measurement for all events. In this example, other root files in the same directory are:

```
ee_dyee1050_2016ULpostVFP.root                      ee_singleantitop_tw_2016ULpostVFP.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_0.root      ee_singletop_tw_2016ULpostVFP.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_1.root      ee_ttbarbg_fromDilepton_2016ULpostVFP.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_2.root      ee_ttbarbg_fromHadronic_2016ULpostVFP.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_3.root      ee_ttbarbg_fromLjets_2016ULpostVFP.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_4.root      ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_0.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_5.root      ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_10.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_6.root      ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_11.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_7.root      ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_12.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_8.root      ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_13.root
ee_dyee50inf_amcatnlofxfx_2016ULpostVFP_9.root      ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_14.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_0.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_15.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_1.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_16.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_2.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_17.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_3.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_18.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_4.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_19.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_5.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_1.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_6.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_2.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_7.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_3.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_8.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_4.root
ee_dyee50inf_madgraphmlm_2016ULpostVFP_9.root       ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_5.root
ee_dymumu1050_2016ULpostVFP.root                    ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_6.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_0.root    ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_7.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_1.root    ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_8.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_2.root    ee_ttbarsignalplustau_fromDilepton_2016ULpostVFP_9.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_3.root    ee_ttbarsignalplustau_fromDilepton_boundstate_2016ULpostVFP.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_4.root    ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_0.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_5.root    ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_10.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_6.root    ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_11.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_7.root    ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_12.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_8.root    ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_13.root
ee_dymumu50inf_amcatnlofxfx_2016ULpostVFP_9.root    ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_14.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_0.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_15.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_1.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_16.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_2.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_17.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_3.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_18.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_4.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_19.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_5.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_1.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_6.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_2.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_7.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_3.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_8.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_4.root
ee_dymumu50inf_madgraphmlm_2016ULpostVFP_9.root     ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_5.root
ee_dytautau1050_2016ULpostVFP.root                  ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_6.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_0.root  ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_7.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_1.root  ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_8.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_2.root  ee_ttbarsignalviatau_fromDilepton_2016ULpostVFP_9.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_3.root  ee_ttbarsignalviatau_fromDilepton_boundstate_2016ULpostVFP.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_4.root  ee_ttbarWjetstolnu_2016ULpostVFP.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_5.root  ee_ttbarWjetstoqq_2016ULpostVFP.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_6.root  ee_ttbarZtollnunu_2016ULpostVFP_0.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_7.root  ee_ttbarZtollnunu_2016ULpostVFP_1.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_8.root  ee_ttbarZtollnunu_2016ULpostVFP_2.root
ee_dytautau50inf_amcatnlofxfx_2016ULpostVFP_9.root  ee_ttbarZtollnunu_2016ULpostVFP_3.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_0.root   ee_ttbarZtollnunu_2016ULpostVFP_4.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_1.root   ee_ttbarZtoqq_2016ULpostVFP_0.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_2.root   ee_ttbarZtoqq_2016ULpostVFP_1.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_3.root   ee_ttbarZtoqq_2016ULpostVFP_2.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_4.root   ee_ttbarZtoqq_2016ULpostVFP_3.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_5.root   ee_ttbarZtoqq_2016ULpostVFP_4.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_6.root   ee_wtolnu_2016ULpostVFP.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_7.root   ee_wwtoall_2016ULpostVFP.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_8.root   ee_wztoall_2016ULpostVFP.root
ee_dytautau50inf_madgraphmlm_2016ULpostVFP_9.root   ee_zztoall_2016ULpostVFP.root
```
dy = drell yan process.
run = actual data.

each one corresponds to a different Feymann diagram. (Ask for confirmation.)

## Root File Structure

## Next Steps
- Try to understand the `framework`, and create combined `histograms` using all relevant root files.
- Use the combined histograms to perform spin correlation analysis, in particular a 2-d plot for Bell observables.
- Obtain information about Bell violation.

### Juan's Feedback
- Look at another computation scheme for the Bell observables, in `arxiv:2205.00542`. 