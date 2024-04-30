from utility.utility import getMostRecentDate, getAllId, filterEntriesById, addValuesToExcel

def handleNewLicenses(wb, registrations):

    sheet = wb['2024']
    recent_date = getMostRecentDate(sheet, "H")
    all_ids = getAllId(sheet)

    filtered_reg = filterEntriesById(all_ids, registrations)

    count = addValuesToExcel(filtered_reg, sheet)

    #current == get first open cell
    