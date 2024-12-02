import os.path
from transmitter import Transmitter

def write_noise_comparison_bits(channel_name, ber, total_bits, total_errors, total_blocks, avg_epr):
    if not os.path.exists("noise_bits.csv"):
        create = open("noise_bits.csv", "w")
        create.write("Channel Name;BER;Total Bits;Total Bit Errors;Total blocks;Average Errors per Block\n")
        create.close()
    file = open("noise_bits.csv","a")
    ber = str(ber).replace(".", ",")
    avg_epr = str(avg_epr).replace(".", ",")
    file.write(channel_name+";"+str(ber)+";"+str(total_bits)+";"+str(total_errors)+";"+str(total_blocks)+";"+avg_epr+"\n")
    file.close()

def write_noise_comparison_bytes(channel_name, ber, total_bytes, total_errors, total_blocks, avg_epr):
    if not os.path.exists("noise_bytes.csv"):
        create = open("noise_bytes.csv", "w")
        create.write("Channel Name;BER;Total Bytes;Total Byte Errors;Total blocks;Average Errors per Block\n")
        create.close()
    file = open("noise_bytes.csv","a")
    ber = str(ber).replace(".", ",")
    avg_epr = str(avg_epr).replace(".", ",")
    file.write(channel_name+";"+str(ber)+";"+str(total_bytes)+";"+str(total_errors)+";"+str(total_blocks)+";"+avg_epr+"\n")
    file.close()

def write_decoding_ratio(channel_name, ber, total_blocks,count_decoded,count_failed):
    if not os.path.exists("decoded_success_ratio.csv"):
        create = open("decoded_success_ratio.csv", "w")
        create.write("Channel Name;BER;Block size;Total Blocks;Decoded Blocks;Failed Blocks;Success Ratio\n")
        create.close()

    ber=str(ber).replace(".",",")
    success_ratio=str(count_decoded/total_blocks).replace(".",",")

    file = open("decoded_success_ratio.csv", "a")
    file.write(str(channel_name)+";"+ber+";"+str(Transmitter.block_size)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+";" + success_ratio+"\n")
    file.close()

def write_noise_comparison_bits_for_GEC(start_state,k,p_to_good,p_to_bad, h, total_bits, total_errors, total_blocks, avg_epr, is_interlaced):
    if not os.path.exists("noise_bits_for_GEC.csv"):
        create = open("noise_bits_for_GEC.csv", "w")
        create.write("Starting State;k;Basic probability to change channel to good;Basic probability to change channel to bad;h;Total Bits;Total Bit Errors;Total blocks;Average Errors per Block;Is interlaced? \n")
        create.close()
    file = open("noise_bits_for_GEC.csv","a")
    avg_epr = str(avg_epr).replace(".", ",")
    file.write(start_state+";"+str(k)+";"+str(p_to_good)+";"+str(p_to_bad)+";"+str(h)+";"+str(total_bits)+";"+str(total_errors)+";"+str(total_blocks)+";"+avg_epr+";"+is_interlaced+"\n")
    file.close()

def write_noise_comparison_bytes_for_GEC(start_state,k,p_to_good, p_to_bad,h, total_bytes, total_errors, total_blocks, avg_epr, is_interlaced):
    if not os.path.exists("noise_bytes_for_GEC.csv"):
        create = open("noise_bytes_for_GEC.csv", "w")
        create.write("Starting State;k;Basic probability to change channel to good;Basic probability to change channel to bad;h;Total Bytes;Total Byte Errors;Total blocks;Average Errors per Block;Is interlaced? \n")
        create.close()
    file = open("noise_bytes_for_GEC.csv","a")
    avg_epr = str(avg_epr).replace(".", ",")
    file.write(start_state+";"+str(k)+";"+str(p_to_good)+";"+str(p_to_bad)+";"+str(h)+";"+str(total_bytes)+";"+str(total_errors)+";"+str(total_blocks)+";"+avg_epr+";"+is_interlaced+"\n")
    file.close()

def write_decoding_ratio_for_GEC(start_state,k,p_to_good,p_to_bad, h, total_blocks,count_decoded,count_failed, is_interlaced):
    if not os.path.exists("decoded_success_ratio_for_GEC.csv"):
        create = open("decoded_success_ratio_for_GEC.csv", "w")
        create.write("Starting State;k;Basic probability to change channel to good;Basic probability to change channel to bad;h;Block size;Total Blocks;Decoded Blocks;Failed Blocks;Success Ratio;Is interlaced?\n")
        create.close()

    success_ratio=str(count_decoded/total_blocks).replace(".",",")

    file = open("decoded_success_ratio_for_GEC.csv", "a")
    file.write(start_state+";"+str(k)+";"+str(p_to_good)+";"+str(p_to_bad)+";"+str(h)+";"+str(Transmitter.block_size)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+";" + success_ratio+";"+is_interlaced+"\n")
    file.close()
   
