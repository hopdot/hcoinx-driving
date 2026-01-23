async function main() {
  const Factory = await ethers.getContractFactory("HCoinXSlotMachine");
  const token = "PASTE_HCX_TOKEN_ADDRESS";
  const contract = await Factory.deploy(token);
  await contract.deployed();
  console.log("Slot Machine deployed to:", contract.address);
}
main();
