<<<<<<< HEAD
import os.path
from transmitter import Transmitter

def write_noise_comparison(channel_name, ber, total_bits, total_errors, total_blocks, avg_epr):
    if not os.path.exists("noise_test.csv"):
        create = open("noise_test.csv", "w")
        create.write("Channel Name;BER;Total Bits;Total Errors;Total blocks;Average Errors per Block\n")
        create.close()
    file = open("noise_test.csv","a")
    file.write(channel_name+";"+str(ber)+";"+str(total_bits)+";"+str(total_errors)+";"+str(total_blocks)+";"+str(avg_epr)+"\n")
    file.close()

def write_decoding(channel_name, ber, total_blocks,count_decoded,count_failed):
    if not os.path.exists("decoded_information.csv"):
        create = open("decoded_information.csv", "w")
        create.write("Channel Name;BER;Block size;Total Blocks;Decoded Blocks;Failed Blocks; Success Ratio\n")
        create.close()
    file = open("decoded_information.csv", "a")
    file.write(str(channel_name)+";"+str(ber)+";"+str(Transmitter.block_size)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+";" + str(count_decoded/(count_decoded+count_failed))+"\n")
=======
import os.path

def write_noise_comparison(channel_name, ber, total_bits, total_errors, total_blocks, avg_epr):
    if not os.path.exists("noise_test.csv"):
        create = open("noise_test.csv", "w")
        create.write("Channel Name;BER;Total Bits;Total Errors;Total blocks;Average Errors per Block\n")
        create.close()
    file = open("noise_test.csv","a")
    file.write(channel_name+";"+str(ber)+";"+str(total_bits)+";"+str(total_errors)+";"+str(total_blocks)+";"+str(avg_epr)+"\n")
    file.close()

def write_decoding(channel_name, ber, total_blocks,count_decoded,count_failed):
    if not os.path.exists("decoded_information.csv"):
        create = open("decoded_information.csv", "w")
        create.write("Channel Name;BER;Total Blocks;Decoded Blocks;Failed Blocks\n")
        create.close()
    file = open("decoded_information.csv", "a")
    file.write(str(channel_name)+";"+str(ber)+";"+str(total_blocks)+";"+str(count_decoded)+";"+str(count_failed)+"\n")
>>>>>>> origin/main
    file.close()