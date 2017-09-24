GLOBAL CLIMATE OBSERVING SYSTEM (GCOS) DIGITAL INVENTORY REPORTS
(Last Updated:  6/11/2014)

1.  INTRODUCTION

    1.1  OVERVIEW

         The Global Climate Observing System (GCOS) Digital Inventory Reports inventory the GCOS Surface Network (GSN) and 
         GCOS Upper Air Network (GUAN) sites that have submitted their surface CLIMAT Messages and Upper Air Data Records
         for processing that have been received by the National Climatic Data Center (NCDC).  Two sets of report files are
         provided, one set of reports for GSN and one set of reports for GUAN.  A description of the report files are
         included below in Section 1.3.

    1.2  ACCESS

         The GCOS Digital Inventory Reports can be accessed at the following location:

         http://www1.ncdc.noaa.gov/pub/data/gcos/

    1.3  DOWNLOADING

         a.  GCOS Surface Network (GSN)

             There are 10 sets of individual files that are included as part of the GCOS Suface Network (GSN) Reports:

          i.     GSN_POR_summary.csv

                 This report provides a summary Of available Surface Hourly Obs (HLY), Synoptic Obs (SYN), and CLIMAT Data (M) 
                 from January 1901 through Present.  Columns of the report are the following:

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digit Station ID (5-digit WMO ID + 1-digit WMO sub-index number to indicate separate station at same location)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.


          ii.    GSN_POR_summary.txt

                 This report provides a summary Of available Surface Hourly Obs (HLY), Synoptic Obs (SYN), and CLIMAT Data (M) 
                 from January 1901 through Present.  Columns of the report are the following:

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digit Station ID (5-digit WMO ID + 1-digit WMO sub-index number to indicate separate station at same location)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.


          iii.   WW_regid_POR_summary.csv

                 regid = WMO Region Association Number {REG1, REG2, REG3, REG4, REG5, REG6, REG7,
                                                        REGX (Unknown Region), ALLREG (All Regions)}
                 
                 This report provides a summary Of available Surface Hourly Obs (HLY), Synoptic Obs (SYN), and CLIMAT Data (M) 
                 from January 1901 through Present.  Columns of the report are the following:

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digits (5-digit WMO ID + 1-digit)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.

                 NOTE:  CLIMAT Data begins around 1990


          iv.    WW_regid_POR_summary.txt

                 regid = WMO Region Association Number {REG1, REG2, REG3, REG4, REG5, REG6, REG7,
                                                        REGX (Unknown Region), ALLREG (All Regions)}
                 
                 This report provides a summary Of available Surface Hourly Obs (HLY), Synoptic Obs (SYN), and CLIMAT Data (M) 
                 from January 1901 through Present.  Columns of the report are the following:

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digit Station ID (5-digit WMO ID + additional value)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.

                 NOTE:  CLIMAT Data begins around 1990


          v.     GSN_types_short_term.txt

                 This file provides summaries of the report types (METAR, SYNOP, etc) in the Integrated Surface Database (ISD).  
                 Column totals in the reports provide hourly counts for the station-year.

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 5-digit WMO ID
                 STATION = Station Name
                 TYPE = Report Type per the following:

                      FM-12 = SYNOP Report from a fixed land station,              SY-AE = Synoptic and aero merged report
                      FM-15 = METAR Aviation routine weather report,               SY-SA = Synoptic and airways merged report,
                      FM-16 = SPECI Aviation selected special weather report,      SY-MT = Synoptic and METAR merged report,
                        SAO = Airways report (includes record specials),           SY-AU = Synoptic and AUTO merged report,
                      SAOSP = Airways special report (excluding record specials),  S-S-A = Synoptic, airways, and AUTO merged,
                       AUTO = Report from an automatic station,                    SA-AU = Airways and AUTO merged report
                      
                 HY = where Y is the hour of observation (H0 is 12 a.m., H1 is 1 a.m.,...H22 is 10 p.m., H23 is 11 p.m.);
                      these columns contain the total count for said hour of observation pertaining to the Report Type.
                 TOTAL = a count of ALL the observations for a month in the Integrated Surface Database (ISD) at NCDC pertaining to
                         the Report Type.


          vi.    GSN_sum_short_term.csv

                 This file contains a complete summary starting with January for the previous year and goes through the 
                 latest available month of data.

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digit Station ID (5-digit WMO ID + additional value)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.


          vii.   GSN_sum_short_term.txt

                 This file contains a complete summary starting with January for the previous year and goes through the 
                 latest available month of data.

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digit Station ID (5-digit WMO ID + additional value)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.


          viii.  GSN_sum_long_term.csv

                 This file contains a complete summary starting in January 2001 through the latest available month of data.

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digit Station ID (5-digit WMO ID + additional value)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.


          ix.    GSN_sum_long_term.txt

                 This file contains a complete summary starting in January 2001 through the latest available month of data.

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 6-digit Station ID (5-digit WMO ID + additional value)
                 Station = Station Name
                 Year = 4-digit Numerical Year (e.g. 2013)
                 HLY = a count of ALL the obs for a month in the Integrated Surface Database (ISD) at NCDC
                 SYN = a count of the SYNOPTIC ob types for a month in the Integrated Surface Database (ISD) at NCDC
                 M = Presence (C) or absence (-) of CLIMAT data in the Monthly Climatic Data for the World (MCDW) at NCDC

                 Each data-month has a HLY, SYN and M column for an overall total of 12 sets of HLY, SYN and M counts.


          x.     GSN_types_YYYY.txt

                 YYYY = 4-digit Numerical Year (e.g. 2013)
                 
                 These files provide summaries of the report types (METAR, SYNOP, etc) in the Integrated Surface Hourly database.  
                 Column totals in the reports provide hourly counts for the station-year.

                 R = WMO Region Association Number (1, 2, 3, 4, 5, 6, 7)
                 WMO = 5-digit WMO ID
                 STATION = Station Name
                 TYPE = Report Type per the following:

                      FM-12 = SYNOP Report from a fixed land station,              SY-AE = Synoptic and aero merged report
                      FM-15 = METAR Aviation routine weather report,               SY-SA = Synoptic and airways merged report,
                      FM-16 = SPECI Aviation selected special weather report,      SY-MT = Synoptic and METAR merged report,
                        SAO = Airways report (includes record specials),           SY-AU = Synoptic and AUTO merged report,
                      SAOSP = Airways special report (excluding record specials),  S-S-A = Synoptic, airways, and AUTO merged,
                       AUTO = Report from an automatic station,                    SA-AU = Airways and AUTO merged report
                      
                 HY = where Y is the hour of observation (H0 is 12 a.m., H1 is 1 a.m.,...H22 is 10 p.m., H23 is 11 p.m.);
                      these columns contain the total count for said hour of observation pertaining to the Report Type.
                 TOTAL = a count of ALL the observations for a month in the Integrated Surface Database (ISD) at NCDC pertaining to
                         the Report Type.


         b.  GCOS Upper Air Network (GUAN)

          i.     GUAN_latest_month.txt

                 This report provides a summary of available upper-air data for the data-month that it's been most recently run for.
                 Columns of the report are the following:

                 R 	 = Region Number
                 WMO	 = WMO Number
                 STATION = Station Name
                 OBS	 = Total Count Of Observations
                 LVLS	 = Total Count of Levels 
                 00Z	 = Count Of Observations at 23Z, 00Z, and 01Z
                 12Z	 = Count of Observations at 11Z, 12Z, and 13Z
                 OTH	 = Count of Observations at All Other Hours
                 AVGPRS	 = Average Pressure At Observation Tops
                 >100	 = Count of Observations Reaching 100 hPa and Above
                 >50	 = Count of Observations Reaching 50 hPa and Above
                 >10	 = Count of Observations Reaching 10 hPa and Above
                 >5	 = Count of Observations Reaching 5 hPa and Above
                 TEMPS	 = Total Levels Containing Temperatures
                 DPDS	 = Total Levels Containing DPD Values
                 WINDS	 = Total Levels Containing Wind Values
                 
                 Summary Report lines are organized by region number and WMO number within region. 


          ii.    GUAN_latest_six_months.txt

                 This report provides a summary of available upper-air data for the most recent 6 data-months that 
                 it's been recently run for.  Columns of the report are the following:

                 R 	 = Region Number
                 WMO	 = WMO Number
                 STATION = Station Name
                 OBS	 = Total Count Of Observations
                 LVLS	 = Total Count of Levels 
                 00Z	 = Count Of Observations at 23Z, 00Z, and 01Z
                 12Z	 = Count of Observations at 11Z, 12Z, and 13Z
                 OTH	 = Count of Observations at All Other Hours
                 AVGPRS	 = Average Pressure At Observation Tops
                 >100	 = Count of Observations Reaching 100 hPa and Above
                 >50	 = Count of Observations Reaching 50 hPa and Above
                 >10	 = Count of Observations Reaching 10 hPa and Above
                 >5	 = Count of Observations Reaching 5 hPa and Above
                 TEMPS	 = Total Levels Containing Temperatures
                 DPDS	 = Total Levels Containing DPD Values
                 WINDS	 = Total Levels Containing Wind Values
                 
                 Summary Report lines are organized by region number and WMO number within region. 


          iii.   GUAN_long_term.txt

                 This report provides a summary of available upper-air data for all data-months since October 2001
                 through the most recent data-month that it's been recently run for.  Columns of the report are the following:

                 R 	 = Region Number
                 WMO	 = WMO Number
                 STATION = Station Name
                 OBS	 = Total Count Of Observations
                 LVLS	 = Total Count of Levels 
                 00Z	 = Count Of Observations at 23Z, 00Z, and 01Z
                 12Z	 = Count of Observations at 11Z, 12Z, and 13Z
                 OTH	 = Count of Observations at All Other Hours
                 AVGPRS	 = Average Pressure At Observation Tops
                 >100	 = Count of Observations Reaching 100 hPa and Above
                 >50	 = Count of Observations Reaching 50 hPa and Above
                 >10	 = Count of Observations Reaching 10 hPa and Above
                 >5	 = Count of Observations Reaching 5 hPa and Above
                 TEMPS	 = Total Levels Containing Temperatures
                 DPDS	 = Total Levels Containing DPD Values
                 WINDS	 = Total Levels Containing Wind Values
                 
                 Summary Report lines are organized by region number and WMO number within region. 

          
2.  DATA

     2.1  METADATA

          The Metadata for GCOS stations are provided by the World Meteorological Organization (WMO).  Please go to the 
          WMO Website at http://www.wmo.int/pages/prog/gcos/index.php?name=ObservingSystemsandData to access the official
          GCOS Metadata.

     2.2  DATA

          GCOS Data (GSN and GUAN) are available for access via the GOSIC Website at http://gosic.org/gcos .

3.  CONTACT
      
     3.1  QUESTIONS AND FEEDBACK
     
          GCOS.NCDC@noaa.gov
          
     3.2  OBTAINING ARCHIVED VERSIONS
     
          At this time, the National Climatic Data Center (NCDC) provides these files to its data partners
          at http://www1.ncdc.noaa.gov/pub/data/gcos/ .  In the future, it is anticipated that NCDC's archival 
          requirements will necessitate the need to archive each run of the GCOS Digital Inventory Reports.

