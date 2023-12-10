from aoc_1 import read_data


def to_binary_str(data: str) -> str:
    """Takes a hex string input and converts it to a binary string representation."""
    return bin(int('1' + data, 16))[3:]


def parse_header(bits: str) -> (int, int):
    """Extract version and type id from a packet. 
    
    Returns:
        A tuple of (version, type ID)
    """
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    return version, type_id


def parse_type4_body(body: str) -> (int, int):
    """Parses the bits of the body (everything minus the header) 5 bits at a time.
    
    Returns:
        Int value of the packet and index of where the data ends.
    """
    ct = 0
    binary_str = ''
    while body and body[0] == "1":
        binary_str = binary_str + body[1:5]
        body = body[5:]
        ct += 1

    return int(binary_str + body[1:5], 2), (ct + 1) * 5


def parse_operator_packet(body: str, typeid: int) -> (str, (int, str)):
    """Takes the body of a subpacket, determines its mode and its contents.
       Parses subpackets and computes their value.
    
    Returns:
        A 2-tuple of remaining data and packet value
    """
    global VERSION_TOTAL
    if len(body) < 11:
        return '', 0

    offset, length_type = (15, 'bits') if body[0] == '0' else (11, 'packets')
    data_start = offset + 1
    
    length = int(body[1: data_start], 2)
    vals = []
    if length_type == 'bits':
        subpacketdata = body[data_start: data_start + length]
        while subpacketdata:
            parse_res = parse(subpacketdata)
            if isinstance(parse_res, int):
                vals.append(parse_res)
            else:
                subpacketdata, val = parse_res
                vals.append(val)

        body = body[data_start + length: ]

    elif length_type == 'packets':
        subpackets = body[data_start: ]
        packet_ct = 0
        while packet_ct < length:
            data, val = parse(subpackets)
            subpackets = data
            packet_ct += 1
            vals.append(val)
    
        body = data

    if typeid == 0:
        op_result = sum(vals)
    elif typeid == 1:
        prod = 1
        for v in vals:
            prod *= v
        op_result = prod
    elif typeid == 2:
        op_result = min(vals)
    elif typeid == 3:
        op_result = max(vals)
    elif typeid == 5:
        op_result = 1 if vals[0] > vals[1] else 0
    elif typeid == 6:
        op_result = 1 if vals[0] < vals[1] else 0
    elif typeid == 7:
        op_result = 1 if vals[0] == vals[1] else 0

    return body, op_result


def parse(data: str) -> (str, int):
    """Recurse though packet data.
    
    Returns:
        A tuple of (data, value)
    """
    if not data or len(data) < 11:
        return data, 0
    
    global VERSION_TOTAL
    vers, typeid = parse_header(data)
    data = data[6:]
    VERSION_TOTAL += vers
    if typeid == 4:
        # type4
        val, idx = parse_type4_body(data)
        data = data[idx:]
        return data, val
    else:
        # operator packetdata
        data, val = parse_operator_packet(data, typeid)
        return data, val


tests = ["110100101111111000101000", "00111000000000000110111101000101001010010001001000000000", 
         "11101110000000001101010000001100100000100011000001100000",
         
         # version total examples
         to_binary_str("8A004A801A8002F478"),  # 16
         to_binary_str("620080001611562C8802118E34"),  # 12
         to_binary_str("C0015000016115A2E0802F182340"), # 23
         to_binary_str("A0016C880162017C3686B18A3D4780"),  # 31
]

# tests
for idx, test in enumerate(tests):
    print(f"Begin Test_{idx}")
    res = parse(test)
    print(f"Test_{idx} result, vers_tot:{VERSION_TOTAL}, val: {res[1]}")
    print('- - - ' * 15)
    VERSION_TOTAL = 0

data = read_data(16)
data = ''.join(data)
bin_str = bin(int('1' + data, 16))[3:]
print(f"Value answer: {parse(to_binary_str(data))[1]}")
print(f"Version answer: {VERSION_TOTAL}")
