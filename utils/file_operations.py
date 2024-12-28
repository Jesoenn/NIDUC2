import os.path
from communication.transmitter import Transmitter


def write_bsc_noise_comparison(channel_quality: str, ber: float, total_symbols: int, total_errors: int, total_blocks: int, avg_epr: float, unit_type: str, code: str):
    if unit_type=="byte":
        file_name="bsc_noise_bytes.csv"
        first_line="Code;Channel Quality;BER;Total Bytes;Total Byte Errors;Total blocks;Average Errors per Block\n"
    elif unit_type=="bit":
        file_name="bsc_noise_bits.csv"
        first_line = "Code;Channel Quality;BER;Total Bits;Total Bit Errors;Total blocks;Average Errors per Block\n"
    else:
        raise Exception("Unit type not supported")

    file_path="./output/csv_exports/"+file_name
    if not os.path.exists(file_path):
        create = open(file_path, "w")
        create.write(first_line)
        create.close()
    file = open(file_path, "a")

    ber = str(ber).replace(".", ",")
    avg_epr = str(avg_epr).replace(".", ",")
    file.write(code+";"+channel_quality + ";" + str(ber) + ";" + str(total_symbols) + ";" + str(total_errors) + ";" + str(
        total_blocks) + ";" + avg_epr + "\n")
    file.close()


def write_decoding_ratio(code: str,channel_quality: str, ber, total_blocks: int,count_decoded: int,count_failed: int, block_size: int, channel_name: str, is_interleaved: str, decoding_type: str):
    file_path="./output/csv_exports/decoded_"+decoding_type+"_success_ratio.csv"
    if not os.path.exists(file_path):
        create = open(file_path, "w")
        create.write("Code;Channel Name;With Interleaving;Channel Quality;BER;Block size;Total "+decoding_type+";Decoded "+decoding_type+";Failed "+decoding_type+";Success Ratio\n")
        create.close()

    ber=str(ber).replace(".",",")
    success_ratio=str(count_decoded/(count_decoded+count_failed)).replace(".",",")

    file = open(file_path, "a")
    file.write(code+";"+str(channel_name)+";"+str(is_interleaved)+";"+str(channel_quality)+";"+ber+";"+str(block_size)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+";" + success_ratio+"\n")
    file.close()

def write_decoding_block_ratio(code: str,channel_quality: str, ber, total_blocks: int,count_decoded: int,count_failed: int, block_size: int, channel_name: str, is_interleaved: str):
    file_path="./output/csv_exports/decoded_blocks_success_ratio.csv"
    if not os.path.exists(file_path):
        create = open(file_path, "w")
        create.write("Code;Channel Name;With Interleaving;Channel Quality;BER;Block size;Total Blocks;Decoded Blocks;Failed Blocks;Success Ratio\n")
        create.close()

    ber=str(ber).replace(".",",")
    success_ratio=str(count_decoded/total_blocks).replace(".",",")

    file = open(file_path, "a")
    file.write(code+";"+str(channel_name)+";"+str(is_interleaved)+";"+str(channel_quality)+";"+ber+";"+str(block_size)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+";" + success_ratio+"\n")
    file.close()

def write_decoding_byte_ratio(code: str,channel_quality: str, ber, total_blocks: int,count_decoded: int,count_failed: int, block_size: int, channel_name: str, is_interleaved: str):
    file_path="./output/csv_exports/decoded_bytes_success_ratio.csv"
    if not os.path.exists(file_path):
        create = open(file_path, "w")
        create.write("Code;Channel Name;With Interleaving;Channel Quality;BER;Block size;Total Bytes;Decoded Bytes;Failed Bytes;Success Ratio\n")
        create.close()

    ber=str(ber).replace(".",",")
    success_ratio=str(count_decoded/total_blocks).replace(".",",")

    file = open(file_path, "a")
    file.write(code+";"+str(channel_name)+";"+str(is_interleaved)+";"+str(channel_quality)+";"+ber+";"+str(block_size)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+";" + success_ratio+"\n")
    file.close()


def write_noise_comparison_bits_for_GEC(start_state,k,p_to_good,p_to_bad, h, total_bits, total_errors, total_blocks, avg_epr, is_interlaced):
    if not os.path.exists("noise_bits_for_GEC.csv"):
        create = open("noise_bits_for_GEC.csv", "w")
        create.write("Starting State;k;Basic probability to change channel to good;Basic probability to change channel to bad;h;Total Bits;Total Bit Errors;Total blocks;Average Errors per Block;Is interlaced? \n")
        create.close()
    file = open("noise_bits_for_GEC.csv","a")
    file.write(start_state+";"+str(k)+";"+str(p_to_good)+";"+str(p_to_bad)+";"+str(h)+";"+str(total_bits)+";"+str(total_errors)+";"+str(total_blocks)+";"+str(avg_epr)+";"+is_interlaced+"\n")
    file.close()

def write_noise_comparison_bytes_for_GEC(start_state,k,p_to_good, p_to_bad,h, total_bytes, total_errors, total_blocks, avg_epr, is_interlaced):
    if not os.path.exists("noise_bytes_for_GEC.csv"):
        create = open("noise_bytes_for_GEC.csv", "w")
        create.write("Starting State;k;Basic probability to change channel to good;Basic probability to change channel to bad;h;Total Bytes;Total Byte Errors;Total blocks;Average Errors per Block;Is interlaced? \n")
        create.close()
    file = open("noise_bytes_for_GEC.csv","a")
    file.write(start_state+";"+str(k)+";"+str(p_to_good)+";"+str(p_to_bad)+";"+str(h)+";"+str(total_bytes)+";"+str(total_errors)+";"+str(total_blocks)+";"+str(avg_epr)+";"+is_interlaced+"\n")
    file.close()

def write_decoding_ratio_for_GEC(start_state,k,p_to_good,p_to_bad, h, total_blocks,count_decoded,count_failed, is_interlaced):
    if not os.path.exists("decoded_success_ratio_for_GEC.csv"):
        create = open("decoded_success_ratio_for_GEC.csv", "w")
        create.write("Starting State;k;Basic probability to change channel to good;Basic probability to change channel to bad;h;Block size;Total Blocks;Decoded Blocks;Failed Blocks;Success Ratio;Is interlaced?\n")
        create.close()
    success_ratio=str(count_decoded/total_blocks)
    file = open("decoded_success_ratio_for_GEC.csv", "a")
    file.write(start_state+";"+str(k)+";"+str(p_to_good)+";"+str(p_to_bad)+";"+str(h)+";"+str(Transmitter.block_size)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+";" + success_ratio+";"+is_interlaced+"\n")
    file.close()

def write_bits_group_error_comparison(error_groups,num_of_error_groups,is_interlaced):
    if not os.path.exists("bits_group_error_comparison.csv"):
        create = open("bits_group_error_comparison.csv", "w")
        create.write("Number of errors in group;Number of errors;Is interlaced? \n ")
        create.close()
    file=open("bits_group_error_comparison.csv","a")
    file.write(str(error_groups)+";"+str(num_of_error_groups)+";"+is_interlaced+"\n")
