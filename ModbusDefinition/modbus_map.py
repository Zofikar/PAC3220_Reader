# -*- coding: utf-8 -*-
"""Auto-generated Modbus register mapping."""

from pymodbus.client import ModbusTcpClient

# Dictionary mapping: index -> (Name, Datatype enum)
REGISTER_MAP = {
    1: (
        "Voltage L1-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    3: (
        "Voltage L2-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    5: (
        "Voltage L3-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    7: (
        "Voltage L1-L2(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    9: (
        "Voltage L2-L3(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    11: (
        "Voltage L3-L1(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    13: (
        "Current L1(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    15: (
        "Current L2(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    17: (
        "Current L3(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    19: (
        "Apparent power L1(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    21: (
        "Apparent power L2(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    23: (
        "Apparent power L3(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    25: (
        "Active power L1(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    27: (
        "Active power L2(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    29: (
        "Active power L3(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    31: (
        "Reactive power L1 (VAR1)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    33: (
        "Reactive power L1 (VAR1)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    35: (
        "Reactive power L1 (VAR1)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    37: (
        "Power factor L1(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    39: (
        "Power factor L2(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    41: (
        "Power factor L3(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    43: (
        "THD-R voltage L1(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    45: (
        "THD-R voltage L2(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    47: (
        "THD-R voltage L3(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    49: (
        "THD-R current L1(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    51: (
        "THD-R current L2(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    53: (
        "THD-R current L3(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    55: (
        "Frequency(Hz)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    57: (
        "Average voltage UL-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    59: (
        "Average voltage UL-L(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    61: (
        "Average current(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    63: (
        "Total apparent power(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    65: (
        "Total active power(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    67: (
        "Total reactive power(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    69: (
        "Total power factor(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    71: (
        "Amplitude unbalance voltage(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    73: (
        "Amplitude unbalance current(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    75: (
        "Maximum voltage L1-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    77: (
        "Maximum voltage L2-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    79: (
        "Maximum voltage L3-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    81: (
        "Maximum voltage L1-L2(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    83: (
        "Maximum voltage L2-L1(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    85: (
        "Maximum voltage L3-L1(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    87: (
        "Maximum current L1(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    89: (
        "Maximum current L2(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    91: (
        "Maximum current L3(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    93: (
        "Maximum apparent power L1(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    95: (
        "Maximum apparent power L2(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    97: (
        "Maximum apparent power L3(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    99: (
        "Maximum active power L1(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    101: (
        "Maximum active power L2(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    103: (
        "Maximum active power L3(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    105: (
        "Maximum reactive power L1 (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    107: (
        "Maximum reactive power L1 (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    109: (
        "Maximum reactive power L1 (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    111: (
        "Maximum power factor L1(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    113: (
        "Maximum power factor L2(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    115: (
        "Maximum power factor L3(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    117: (
        "Maximum THD-R voltage L1-L2(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    119: (
        "Maximum THD-R voltage L2-L3(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    121: (
        "Maximum THD-R voltage L3-L1(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    123: (
        "Maximum THD-R current L1(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    125: (
        "Maximum THD-R current L2(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    127: (
        "Maximum THD-R current L3(%)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    129: (
        "Maximum frequency(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    131: (
        "Maximum average voltage UL-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    133: (
        "Maximum average voltage UL-L(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    135: (
        "Maximum average current(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    137: (
        "Maximum total apparent power(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    139: (
        "Maximum total active power(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    141: (
        "Maximum total reactive power (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    143: (
        "Maximum total power factor(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    145: (
        "Minimum voltage L1-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    147: (
        "Minimum voltage L2-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    149: (
        "Minimum voltage L3-N(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    151: (
        "Minimum voltage L1-L2(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    153: (
        "Minimum voltage L2-L1(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    155: (
        "Minimum voltage L3-L1(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    157: (
        "Minimum current L1(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    159: (
        "Minimum current L2(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    161: (
        "Minimum current L3(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    163: (
        "Minimum apparent power L1(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    165: (
        "Minimum apparent power L2(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    167: (
        "Minimum apparent power L3(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    169: (
        "Minimum active power L1(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    171: (
        "Minimum active power L2(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    173: (
        "Minimum active power L3(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    175: (
        "Minimum reactive power L1 (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    177: (
        "Minimum reactive power L1 (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    179: (
        "Minimum reactive power L1 (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    181: (
        "Minimum power factor L1(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    183: (
        "Minimum power factor L2(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    185: (
        "Minimum power factor L3(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    187: (
        "Minimum frequency(Hz)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    189: (
        "Minimum average voltage UL(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    191: (
        "Minimum average voltage UL-L(V)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    193: (
        "Minimum average current(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    195: (
        "Minimum total apparent power(VA)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    197: (
        "Minimum total active power(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    199: (
        "Minimum total reactive power (VARn)(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    201: (
        "Minimum total power factor(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    203: (
        "Limit violations(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    205: (
        "PMD diagnostics and status(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    207: (
        "Digital outputs status(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    209: (
        "Digital inputs status(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    211: (
        "Active tariff(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    213: (
        "Operating hours counter(s)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    215: (
        "Counter (configurable)(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    217: (
        "Counter basic parameter changes(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    219: (
        "Counter all parameter changes(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    221: (
        "Counter limit value changes(–)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    223: (
        "Current N(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    225: (
        "Maximum current N(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    227: (
        "Minimum current N(A)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    231: (
        "Configurable energy counter(kWh)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    233: (
        "Status digital outputs module 1(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    235: (
        "Status digital inputs module 1(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    237: (
        "Status digital outputs module 2(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    239: (
        "Status digital inputs module 2(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    501: (
        "Cumulated average active power import(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    503: (
        "Cumulated average reactive power import(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    505: (
        "Cumulated average active power export(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    507: (
        "Cumulated average reactive power export(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    509: (
        "Maximum active power reading during demand period(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    511: (
        "Minimum active power reading during demand period(W)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    513: (
        "Maximum reactive power reading during demand period(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    515: (
        "Minimum reactive power reading during demand period(var)",
        ModbusTcpClient.DATATYPE.FLOAT32
    ),
    517: (
        "Length of the current demand period(s)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    519: (
        "Time since start of current demand period(s)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    799: (
        "Date/time(–)",
        ModbusTcpClient.DATATYPE.UINT32
    ),
    801: (
        "Total active energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    805: (
        "Total active energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    809: (
        "Total active energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    813: (
        "Total active energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    817: (
        "Total reactive energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    821: (
        "Total reactive energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    825: (
        "Total reactive energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    829: (
        "Total reactive energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    833: (
        "Total apparent energy tariff 1(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    837: (
        "Total apparent energy tariff 2(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    841: (
        "L1 active energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    845: (
        "L1 active energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    849: (
        "L1 active energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    853: (
        "L1 active energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    857: (
        "L1 reactive energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    861: (
        "L1 reactive energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    865: (
        "L1 reactive energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    869: (
        "L1 reactive energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    873: (
        "L1 apparent energy tariff 1(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    877: (
        "L1 apparent energy tariff 2(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    881: (
        "L2 active energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    885: (
        "L2 active energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    889: (
        "L2 active energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    893: (
        "L2 active energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    897: (
        "L2 reactive energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    901: (
        "L2 reactive energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    905: (
        "L2 reactive energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    909: (
        "L2 reactive energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    913: (
        "L2 apparent energy tariff 1(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    917: (
        "L2 apparent energy tariff 2(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    921: (
        "L3 active energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    925: (
        "L3 active energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    929: (
        "L3 active energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    933: (
        "L3 active energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    937: (
        "L3 reactive energy import tariff 1(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    941: (
        "L3 reactive energy import tariff 2(Wh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    945: (
        "L3 reactive energy export tariff 1(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    949: (
        "L3 reactive energy export tariff 2(varh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    953: (
        "L3 apparent energy tariff 1(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
    957: (
        "L3 apparent energy tariff 2(VAh)",
        ModbusTcpClient.DATATYPE.FLOAT64
    ),
}

REGISTER_NAME_TO_ADDRESS = (lambda: {value[0]: idx for idx, value in REGISTER_MAP.items()})()
