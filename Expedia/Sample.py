#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

#define sample's count here
sampleCount = 100;
with open( 'F:/UTD/Match/Kaggle/train.csv','rb') as r:
    r.readline()
    count = 1;
    out = open('./data.csv', "w")
    out.write("date_time, site_name, posa_continent, user_location_country, user_location_region, user_location_city, orig_destination_distance, user_id, is_mobile, is_package, channel, srch_ci, srch_co, srch_adults_cnt, srch_children_cnt, srch_rm_cnt, srch_destination_id, srch_destination_type_id, is_booking, cnt, hotel_continent, hotel_country, hotel_market, hotel_cluster\n")
    while(count<=sampleCount):
        line = r.readline().strip()
        print line
        count += 1
        arr = line.split(",")
        length = len(arr)
        for i in range(0,length-1):
            #print str(arr[i]+',')
            out.write(str(arr[i])+',')
        #print  str(arr[length-1])
        out.write(str(arr[length-1]))
        out.write("\n")
            #out.write(str(user_location_country) + ','+str())
        
        
out.close()
r.close()



