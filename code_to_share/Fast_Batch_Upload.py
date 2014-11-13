# coding=utf-8
"""
Used as a scratch script for developing ISEA upload tool
"""
import time
try:
    import os
    from arcpy import GetParameterAsText, ArcSDESQLExecute, env, InsertCursor, Append_management, Delete_management
    from arcpy.da import NumPyArrayToTable
    import numpy as np
    import logging
    import copy
    from datetime import datetime as dt

## Setup a log file, Arc's traceback and such
## is shit.


## Change this back!
    logging.basicConfig(filename = r'C:\Users\justin_grana\Desktop\uploadlog.log',
                    level=logging.DEBUG)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logging.info(time.strftime(now) + ' The Log Has Been Created. \n')



    ## Directory of CSV Files to Upload
    csv_dir=GetParameterAsText(0)
    ## Path to SDE file
    sde_file = GetParameterAsText(1)
    #csv_dir = 'C:\\Users\\justin_grana\\Desktop\\test_csv_dir'

#try:
#    sde_file = '\\C:\\Users\\justin_grana\\Desktop\\Connection_to_Isea.sde'
#except Exception:
#    sde_file = unicode('C:\Users\justin_grana\Desktop\Connection_to_Isea.sde')
#print sde_file
#print csv_dir
except Exception as e:
    print e
    time.sleep(20)
    raise
    


def update(directory, sde):
    """

    directory : str
        Path to folder containing CSV files to upload

    sde : str
        Path to database file to connect to

    """
    try: 
        files = os.listdir(directory)
        ## Need to Change these when I pass over to Serene STILL TRUE
        isea_table =  'sde_ISEA.DBO.ISEADATA'
        version_table = 'sde_ISEA.SDE_ADMIN.Versions'
        full_version_path = sde  + '\\' + version_table
        full_data_path = sde + '\\' + isea_table
        #######################################################
        sdeConn = ArcSDESQLExecute(sde)
        ## Get the current max version ##
        sql_max_version = 'SELECT MAX(VersionID) FROM ' + version_table
        max_id = int(sdeConn.execute('Select MAX(ObjectID) FROM ' +isea_table))
        sql_max_version = unicode(sql_max_version)
        max_version = sdeConn.execute(sql_max_version)
        all_variables_sql = 'SELECT VariableName FROM ' + unicode(version_table)
        all_variables_sql = unicode(all_variables_sql)
        print all_variables_sql, max_version
        temp_varlist = sdeConn.execute(all_variables_sql)
        varlist = [x[0] for x in temp_varlist]
        # Used to create structured arrays
        names='VersionID,ZipCode,VariableName,VariableValue,IsCurrent'
        formats='i4,S10,S32,f8,i2'
        ## Begin Looping Through Files in Directory
        ## Consistent file naming is essential
        for f in files:
            start = time.time() # Time it
            f_split = f.split("_")
            yr = f_split[-2]
            mth = f_split[-1].split(".")[0]
            valid_to = mth + '/' + '1' + '/' + yr
            data = np.genfromtxt(directory + '\\' + f, delimiter=',', names=True)
            variable_names = list(copy.copy(data.dtype.names))
            ### Might not be necessary.  Can't be immutable
            zip_temp = list(data['zipcode'])
            zips = [str('0000'+ str(int(x)))[-5:] for x in zip_temp]
            

            
            

            ## Remove non-variable columns
            variable_names.remove('zipcode')
            variable_names.remove('year')
            variable_names.remove('month')
            variable_names.remove('county')
            variable_names.remove('county_fips')
            variable_names.remove('state_code')
            variable_names.remove('area')

            for var in variable_names:
                varstart = time.time()
                max_version += 1
                ## Lets check to see if they are all nan
                if np.all(np.isnan(data[var])):
                    # Don't do anything with variables with no data'
                    pass
                else:
                    if np.any(np.isnan(data[var])):
                        logging.warning('The variable ' + var + \
                                        ' in ' + f + ' is not empty but ' + \
                                        'has missing observations')
                    v_split = var.split('_')
                    if len(v_split) == 2:
                        FreqType = 'Monthly_Level'
                        if int(mth) != int(1) :
                            valid_from = str(int(mth) - 1)+ '/' + '1' + '/' + yr
                        else:
                            valid_from = '12' + '/' + '1' + '/' + str(int(yr) -1 )
                    elif v_split[-1]=='dy':
                        FreqType = 'Annual'
                        valid_from = mth+ '/' + '1' + '/' + str(int(yr) - 1)
                    elif v_split[-1] =='dm':
                        FreqType = 'Monthly'
                        if int(mth) != int(1) :
                            valid_from = str(int(mth) - 1)+ '/' + '1' + '/' + yr
                        else:
                            valid_from = '12' + '/' + '1' + '/' + str(int(yr) -1 )
                    elif v_split[-1] =='c':
                        FreqType = 'Categorical'
                        if int(mth) != int(1) :
                            valid_from = str(int(mth) - 1)+ '/' + '1' + '/' + yr
                        else:
                            valid_from = '12' + '/' + '1' + '/' + str(int(yr) -1 )
                    else :
                        FreqType = v_split[-1]
                        logging.warning('The variable' + var + \
                                        ' in ' + f + 'has a frequency' + \
                                            ' that cannot be determined')
                    
                    # Let's see if data is already loaded
                    # Checks by matching variable name and
                    # valid dates.
                    # print valid_to, valid_from, str(int(mth))
                    check_duplicate_sql = 'SELECT VersionID FROM ' + \
                                          version_table  +' WHERE ' +\
                                          'CAST(VariableName as varchar(8000))=\''+var + '\' AND ' + \
                                          'ValidTo=\' '+str(valid_to) +'\' AND ' + \
                                          'ValidFrom=\'' +str(valid_from)+'\''
                    isduped = sdeConn.execute(check_duplicate_sql)
                    if isduped != True:
                        logging.critical('The variable ' + var + \
                                        ' in ' + f + ' seems to  have ' + \
                                          ' already been uploaded with version ID ' + \
                                           str(isduped) + ' Variable ' +  \
                                          ' reuploaded with new version number ' + str(max_version))
                    ## Now let's update the versions table.

                    ## For some reason, passing an INSERT statement
                    ## through Arcpy throws a unicode error.  Not
                    ## sure why this happens,  An update of Arc might
                    ## fix this.  Otherwise, it might be necessary
                    ## to contact Arc.

                        
                    #inserted_tup = str((str(new_version), now,
                    #                str(valid_from), str(valid_to),
                    #                FreqType,var))
                    #inserted_tup = u'('+u'\'' + unicode(var) + u'\')'
                    #print inserted_tup
                    #columns = str(('VersionID', 'DateImported', 'ValidFrom',
                    #               'ValidTo', 'FreqType', 'VariableName'))
                    #columns = u'(' + u'\'' + u'VariableName\')'
                    #columns = columns.encode('utf-8')
                    #update_versions = u'INSERT INTO ' + unicode(version_table) + u' ' +\
                    #                   columns +u' VALUES ' + inserted_tup
                    #update_versions = unicode(update_versions)
                    #update_versions = unicode("INSERT INTO sde_ISEA.SDE_ADMIN.Versions (\'VariableName\') VALUES (\'msc_crempzip_dm\')")
                    #print update_versions
                    #try :
                    #    sdeConn.execute(update_versions)
                    #except Exception as e:
                    #    print e
                    #    time.sleep(50)
                    # This works, just uncomment while I Dev'

                    rowsVer = InsertCursor(full_version_path)
                    rowVer = rowsVer.newRow()
                    rowVer.setValue("VersionID", str(max_version))
                    rowVer.setValue("DateImported", now)
                    rowVer.setValue("ValidFrom", valid_from )
                    rowVer.setValue("ValidTo", valid_to)
                    rowVer.setValue("FreqType", FreqType)
                    rowVer.setValue("VariableName", var)
                    rowsVer.insertRow(rowVer)

                    ### Now let's add to the ISEA table

                    ## First figure out if the variable has already been loaded
                    ## if not, make it as current
                    ## if yes, find the validto date of the current
                    ## if vars valid_to after is_current version
                    ## make this current and other one not current
                    ## otherwise make this not current.

                    ## NB: It seems the only way to add rows to a
                    ## sql table is to loop through.  This is going
                    ## to be very slow.  That said, it might make sense to
                    ## actually read the entire database into memory,
                    ## append to it and then spit it back out...tbd.
                    isCurrent=1
                    if not (var in varlist):
                        isCurrent = 1

                    else:
                        dt_var = dt.strptime(valid_to, "%m/%d/%Y")
                        sql_get_valid_to = 'SELECT ValidTo FROM ' + version_table + \
                                ' WHERE CAST(VariableName as varchar(8000))=\''+var + '\''
                        prev_valid_to = sdeConn.execute(sql_get_valid_to)
                        print prev_valid_to
                        if type(prev_valid_to) == unicode:
                            prev_dt = dt.strptime(prev_valid_to, "%m/%d/%Y")
                            if prev_dt > dt_var:
                                isCurrent = 0
                        if type(prev_valid_to) != unicode: #list or tuple:
                            for vt in prev_valid_to:
                                vt=vt[0]
                                # This is a bit greedy and can be improved
                                prev_dt = dt.strptime(vt, "%m/%d/%Y")
                                if prev_dt > dt_var:
                                    # Note no equals sign
                                    isCurrent=0
                        if isCurrent == 1:  # If actually is current, need to adjust othes
                            sql_not_current = 'UPDATE ' + isea_table + ' SET IsCurrent=\'0\' WHERE ' + \
                                              'VariableName=\'' + var +'\';'
                            sdeConn.execute(sql_not_current)
                            print sql_not_current
                    #datarowsVer = InsertCursor(full_data_path)
                    print 'Starting to add to ISEA'
                    arrdata =  np.array([[max_version]*len(zips), zips, [var]*len(zips), list(data[var]), [isCurrent]*len(zips)])
                    sarr = np.core.records.fromarrays(arrdata,
                                      names=names,
                                      formats=formats)
            
                    NumPyArrayToTable(sarr, r'C:\Users\justin_grana\Desktop\Connection_to_isea.sde\temptable')
            
                    Append_management(r'C:\Users\justin_grana\Desktop\Connection_to_isea.sde\temptable',
                                            full_data_path)
                    Delete_management(r'C:\Users\justin_grana\Desktop\Connection_to_isea.sde\temptable')
                    

    ##                for ix in range(len(zips)):
    ##                    max_id += 1
    ##
    ##                    #print max_version, zips[ix], var, data[var][ix]
    ##                    #datarowVer = datarowsVer.newRow()
    ##                    #datarowVer.setValue("VersionID", str(max_version))
    ##                    #datarowVer.setValue("ZipCode", zips[ix])
    ##                    #datarowVer.setValue("VariableName", var )
    ##                    #datarowVer.setValue("VariableValue", data[var][ix] )
    ##                    #datarowVer.setValue("IsCurrent", str(isCurrent))
    ##                    #datarowsVer.insertRow(datarowVer)
    ##                    #print 'finished a row'
    ##
    ##                    # I think the sql statement way will be more robust
    ##                    # and faster
    ##
    ##                    ## FOr some reason the Object ID field is not automatically updating,
    ##                    ## not sure why.  Will update manually.
    ##                    if not np.isnan(data[var][ix]):
    ##			variable_value = '%f' % data[var][ix]
    ##                        sql_isea_row = "INSERT INTO " + isea_table + \
    ##                                   ' (ObjectID, VersionID, ZipCode, VariableName, VariableValue, IsCurrent) ' + \
    ##                                   ' VALUES (\''+ str(max_id) + '\', \' ' + str(max_version) +'\', \'' +str(zips[ix]) + '\', \'' +\
    ##                                    var + '\', \'' + variable_value +'\', \'' + str(isCurrent) + '\')'
    ##                    else:
    ##                        sql_isea_row = "INSERT INTO " + isea_table + \
    ##                                   ' (ObjectID, VersionID, ZipCode, VariableName, IsCurrent) ' + \
    ##                                   ' VALUES (\''+ str(max_id) + '\', \' ' + str(max_version) +'\', \'' +str(zips[ix]) + '\', \'' +\
    ##                                    var + '\', \'' + str(isCurrent) + '\')'
    ####                    sql_isea_row = "INSERT INTO " + isea_table + \
    ####                                   ' VALUES (\''+str(max_version) +'\', \'' +str(zips[ix]) + '\', \' ' +\
    ####                                    var + '\', \'' + str(data[var][ix]) +'\', \'' + str(isCurrent) + '\')'
    ##
    ##                    try:
    ##			sdeConn.execute(sql_isea_row)
    ##		    except Exception:
    ##			print ix
    ##			print sql_isea_row
    ##			time.sleep(25)
    ##			raise
    ##                    if ix %1000 ==0:
    ##                        print ix
                    print 'One variable takes', time.time() - varstart
    except Exception as e:
        print(e)
        time.sleep(20)
    return 'Done'

                    

                
                
                
        #print 'one file takes', start-time.time()
        
try :
    update(csv_dir, sde_file)
    print('success')
    time.sleep(10)
except Exception as e:
    print e
    time.sleep(10)
    logging.exception('Error Traceback:')
    time.sleep(10)
    raise
