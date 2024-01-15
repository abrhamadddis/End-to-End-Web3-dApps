 # End-to-End Web3 dApps: certificate generation, distribution, and value transfer with Algorand NFTs and smart contracts

 End-to-End Web3 dApps: certificate generation, distribution, and value transfer with Algorand NFTs and smart contracts

 **Table of Contents**
 - [End to End Web3 dApps](#End to End Web3 dApps)
  - [Overview](#overview)
  - [About](#about)
  - [Project Structure](#project-structure)
    - [.github](#.github)
    - [notebooks](#notebooks)
    - [scripts](#scripts)
    - [tests](#tests)
    - [root folder](#root-folder)
  - [Installation guide](#Installation-guide)

  ## Overview

Develop comprehensive decentralized applications (dApps) on the Algorand Blockchain for 10 Academy, enabling the creation and distribution of Non-Fungible Tokens (NFTs) as certificates. These NFTs will symbolize the successful completion of weekly challenges for trainees. Additionally, the dApps will empower trainees possessing these NFTs to engage with a smart contract, facilitating the execution of predefined actions.

## About

The objective of this project, commissioned by 10 Academy, is to address the challenge of securely providing certificates to all trainees. The current distribution method involves issuing simple PDF files, lacking mechanisms for verifying authenticity. The client seeks a solution that not only ensures secure certificate distribution but also explores the possibility of enabling certificate holders to engage in smart contract actions, both presently and in the future. This marks a significant enhancement from the current practice, where certificates are static PDFs and lack interactive features or verification capabilities.

## Why Algorand

Algorand sets itself apart with Pure Proof-of-Stake consensus for decentralization and speed. It features Algorand Standard Assets for token creation and Algorand Smart Contracts for executing decentralized applications. Emphasizing security and openness, Algorand supports atomic transfers and aims to prevent node power concentration.

## Project Structure

Here's a brief overview of the directory structure:

1. **Root Directory**: This is the top-level directory of your project. It contains configuration files like `.gitignore` and `Readme.md`, which provide an overview and instructions for the project.

2. **Fullstack Directory**: This directory contains the backend and frontend components of the project.

3. **Image Directory**: This directory contains various image files related to the project.

4. **Image-Generation Directory**: This directory contains Python scripts for generating and editing images.

5. **Note-Books Directory**: This directory contains Jupyter notebooks related to the project.

## Installation guide

React Frontend
```
git clone https://github.com/abrhamadddis/End-to-End-Web3-dApps
cd End-to-End-Web3-dApps/fullstack/frontend
npm install
npm start
```

![Alt text](./image/front_end.png?raw=true "front end")

Backend Server
```
git clone https://github.com/abrhamadddis/End-to-End-Web3-dApps
cd End-to-End-Web3-dApps/fullstack/backend/smart_contracts/certificate/
python contract.py 
```

![Alt text](./image/dappflow.png?raw=true "Back end")

## Collaborators

- [Abhram Addis](https://github.com/abrhamadddis)
