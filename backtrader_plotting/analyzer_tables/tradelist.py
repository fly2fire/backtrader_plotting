from backtrader_plotting.bokeh.datatable import ColummDataType


def datatable(self):
    tables = []
    tab1 = [['ref', ColummDataType.INT],
             ['ticker', ColummDataType.STRING],
             ['dir', ColummDataType.STRING],
             ['datein', ColummDataType.DATETIME],
             ['pricein', ColummDataType.FLOAT],
             ['dateout', ColummDataType.DATETIME],
             ['priceout', ColummDataType.FLOAT],
             ['chng%', ColummDataType.FLOAT],
             ['pnl', ColummDataType.FLOAT],
             ['pnl%', ColummDataType.FLOAT],
             ['size', ColummDataType.FLOAT],
             ['value', ColummDataType.FLOAT],
             ['cumpnl', ColummDataType.FLOAT],
             ['nbars', ColummDataType.FLOAT],
             ['pnl/bar', ColummDataType.FLOAT],
             ['mfe%', ColummDataType.FLOAT],
             ['mae%', ColummDataType.FLOAT],
             ]

    trade_list = self.get_analysis()
    for a in trade_list:
        tab1[0].append(a['ref'])
        tab1[1].append(a['ticker'])
        tab1[2].append(a['dir'])
        tab1[3].append(a['datein'])
        tab1[4].append(a['pricein'])
        tab1[5].append(a['dateout'])
        tab1[6].append(a['priceout'])
        tab1[7].append(a['chng%'])
        tab1[8].append(a['pnl'])
        tab1[9].append(a['pnl%'])
        tab1[10].append(a['size'])
        tab1[11].append(a['value'])
        tab1[12].append(a['cumpnl'])
        tab1[13].append(a['nbars'])
        tab1[14].append(a['pnl/bar'])
        tab1[15].append(a['mfe%'])
        tab1[16].append(a['mae%'])
    tables.append(tab1)

    return "Trade List", tables
