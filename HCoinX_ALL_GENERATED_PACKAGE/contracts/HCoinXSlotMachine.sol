// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HCoinXSlotMachine {
    IERC20 public hcx;
    address public owner;
    uint256 public spinCost = 10 * 1e18;

    event Spin(address indexed player, bool win);

    constructor(address _hcx) {
        hcx = IERC20(_hcx);
        owner = msg.sender;
    }

    function spin() external {
        require(hcx.transferFrom(msg.sender, address(this), spinCost), "Payment failed");
        bool win = (uint256(blockhash(block.number - 1)) % 10 == 0);
        if (win) {
            hcx.transfer(msg.sender, spinCost * 5);
        }
        emit Spin(msg.sender, win);
    }
}
