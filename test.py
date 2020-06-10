from utils import *
import torch
from dgl import model_zoo
from rdkit import Chem
import rdkit.Chem.Draw as Draw
import pubchempy as pc

model = model_zoo.chem.GCNClassifier(
        in_feats=74,
        gcn_hidden_feats=[64 for _ in range(2)],
        n_tasks=12,
        classifier_hidden_feats=64)
model.load_state_dict(torch.load("./model/early_stop_2020-06-10_14-46-25.pth")['model_state_dict'])
model.eval()
with torch.no_grad():
        samplename = input("Please input the compound's name\n")
        print(samplename)
        results = pc.get_compounds(samplename, 'name')
        if not results:
                print("No information")
                raise SystemExit
        print (results)
        for compound in results:
                testsample = compound.canonical_smiles
                if(testsample==0):
                        print("No information")
                        raise SystemExit
                m = Chem.MolFromSmiles(testsample)
                a = Draw.MolToImage(m,(600,600))
                a.show()
                sample = smile_to_bigraph(testsample)
                atom_feature = sample.ndata.pop('h')
                predictions = model(sample,atom_feature)
                predictions = torch.nn.Sigmoid()(predictions)
                print(predictions)
