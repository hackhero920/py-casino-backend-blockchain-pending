## Installation

1. Make sure [Python 3.7+](https://www.python.org/downloads/) is installed. 
2. Git Clone
```
$ git clone https://github.com/Carlos-Zen/blockchain.git
$ cd blockchain
```

## Usage

- Create Account
```
$ python console account create
```
- Run the miner
```
$ python console miner start 3008
```
- Transaction transfer.   
```
$ python console tx transfer from_address to_address amount
```
- Transaction list.   
```
$ python console tx list
```
- Blockchain shows.   
```
$ python console blockchain list
```
### Node Network
Copy the code resource to a new directory.While the miner before was running then:
```
$ cd {another_blockchain_directory}
$ python console node add 3008 
$ python console node run 3009
```
When a new block mined , block and transactions will broadcast to other nodes.

## All command
Use like this:   

```
$ python console [module] [action] params...
```
Such as:
```
$ python console tx list
```
