# Gedit Plugins
Collection of Gedit plugins:
1. [JSON Formatter](#JSON-Formatter): Verify, Format and Minify json documents
2. [Prettifier](#Prettifier): Prettify data structures

---

<div>
    <img 
        style="display: block; 
               margin-left: auto;
               margin-right: auto;
               width: 75%;"
        src="./media/gedit-plugin-collection.jpg" 
        alt="Gedit plugin collection">
</div>

---

## Installation
1. Get the file `gedit-plugin-collection-x.y.z.tar.gz` from the latest [release](https://github.com/Elnaril/gedit-plugin-collection/releases)
2. Extract its content into the folder `~/.local/share/gedit/plugins`

So you should have something similar to:
```bash
.local/share/gedit/
└── plugins
    ├── jsonformatter/
    ├── jsonformatter.plugin
    ├── prettifier/
    └── prettifier.plugin
```

3. Activate the plugin(s) you wish in the Gedit Preferences window.

## JSON Formatter

This plugin allows you to easily:
- Verify (CTRL-ALT-v) a JSON document is a correctly formatted 
- Format (CTRL-ALT-J) a JSON document
- Minify (CTRL-ALT-j) a JSON document

#### Format Example:
```json
[
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "initialOwner",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    }
]
```
#### Minify Example:
```json
[{"inputs": [{"internalType": "address", "name": "initialOwner", "type": "address"}], "stateMutability": "nonpayable", "type": "constructor"}]
```

## Prettifier
This plugin allows you to make readable data structures defined with {, [, ", ...  
Keyboard shortcut: CTRL-SHIFT-P

Let's say you have this document:
```text
<Function execute(bytes,bytes[],uint256)>{ 'commands': b'\x10', 'inputs': [ ( <Function V4_SWAP(bytes,bytes[])>, { 'actions': b'\x06\x0f\x0c', 'params': [ ( <Function SWAP_EXACT_IN_SINGLE(((address,address,uint24,int24,address),bool,uint128,uint128,bytes))>, { 'exact_in_single_params': { 'PoolKey': { 'currency0': '0x0000000000000000000000000000000000000000', 'currency1': '0xBf5617af623f1863c4abc900c5bebD5415a694e8', 'fee': 3000, 'tickSpacing': 50, 'hooks': '0x0000000000000000000000000000000000000000' }, 'zeroForOne': False, 'amountIn': 100000000000000, 'amountOutMinimum': 798750268136655870501951828, 'hookData': b'' } } ), ( <Function TAKE_ALL(address,uint256)>, { 'currency': '0x0000000000000000000000000000000000000000', 'minAmount': 0 } ), ( <Function SETTLE_ALL(address,uint256)>, { 'currency': '0xBf5617af623f1863c4abc900c5bebD5415a694e8', 'maxAmount': 100000000000000 } ) ] }, { 'revert_on_fail': True } ) ], 'deadline': 1732612928}
```

You can get it formatted like that:
```text
<Function execute(bytes,bytes[],uint256)>
{
    'commands': b'\x10',
    'inputs': [
        (
            <Function V4_SWAP(bytes,bytes[])>,
            {
                'actions': b'\x06\x0f\x0c',
                'params': [
                    (
                        <Function SWAP_EXACT_IN_SINGLE(((address,address,uint24,int24,address),bool,uint128,uint128,bytes))>,
                        {
                            'exact_in_single_params': {
                                'PoolKey': {
                                    'currency0': '0x0000000000000000000000000000000000000000',
                                    'currency1': '0xBf5617af623f1863c4abc900c5bebD5415a694e8',
                                    'fee': 3000,
                                    'tickSpacing': 50,
                                    'hooks': '0x0000000000000000000000000000000000000000'
                                    
                                },
                                'zeroForOne': False,
                                'amountIn': 100000000000000,
                                'amountOutMinimum': 798750268136655870501951828,
                                'hookData': b''
                                
                            } 
                        } 
                    ),
                    (
                        <Function TAKE_ALL(address,uint256)>,
                        {
                            'currency': '0x0000000000000000000000000000000000000000',
                            'minAmount': 0 
                        } 
                    ),
                    (
                        <Function SETTLE_ALL(address,uint256)>,
                        {
                            'currency': '0xBf5617af623f1863c4abc900c5bebD5415a694e8',
                            'maxAmount': 100000000000000 
                        } 
                    ) 
                ] 
            },
            {
                'revert_on_fail': True 
            } 
        ) 
    ],
    'deadline': 1732612928
}
```
