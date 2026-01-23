# Create GitHub Actions workflow + PC-ready package

import os, zipfile, textwrap

base = "/mnt/data/HCoinX_PC_GITHUB_AUTODEPLOY"
os.makedirs(base + "/.github/workflows", exist_ok=True)
os.makedirs(base + "/contracts", exist_ok=True)
os.makedirs(base + "/frontend", exist_ok=True)

workflow = """name: HCoinX Auto Deploy

on:
  push:
    branches: [ "main" ]

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repo
      uses: actions/checkout@v4

    - name: Setup Node
      uses: actions/setup-node@v4
      with:
        node-version: '18'

    - name: Install Dependencies
      run: npm install

    - name: Compile Contracts
      run: npx hardhat compile

    - name: Deploy to Ethereum (Alchemy)
      env:
        ALCHEMY_API_KEY: ${{ secrets.ALCHEMY_API_KEY }}
        PRIVATE_KEY: ${{ secrets.DEPLOYER_PRIVATE_KEY }}
      run: npx hardhat run scripts/deploy.js --network mainnet
"""

readme = """# HCoinX PC + GitHub Auto Deploy Package

## Auto Deploy
- Push to `main`
- GitHub Actions deploys via Alchemy

## Required Secrets
- ALCHEMY_API_KEY
- DEPLOYER_PRIVATE_KEY

## Usage
1. Unzip on PC
2. Open folder
3. Push to GitHub (@hopdot)
4. Add secrets
5. Push changes → auto deploy

## Frontend
Static HTML for Wix, Google Cloud, Render
"""

deploy_script = """async function main() {
  const HCX = await ethers.getContractFactory("HCoinXSlotMachine");
  const hcxToken = "PASTE_TOKEN_ADDRESS";
  const contract = await HCX.deploy(hcxToken);
  await contract.deployed();
  console.log("Slot deployed:", contract.address);
}
main();
"""

open(base + "/.github/workflows/deploy.yml","w").write(workflow)
open(base + "/README.md","w").write(readme)
open(base + "/scripts_deploy.js","w").write(deploy_script)

zip_path = "/mnt/data/HCoinX_PC_AUTO_DEPLOY.zip"
with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    for root,_,files in os.walk(base):
        for f in files:
            full = os.path.join(root,f)
            z.write(full, arcname=full.replace(base+"/",""))

zip_path
