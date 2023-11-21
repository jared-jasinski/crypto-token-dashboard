import time

import mysql.connector
from mysql.connector import cursor


def add(token_stats, channel_name):
    calltime = 1000 * time.time()

    # Extract the relevant values from the dictionary
    pair = token_stats['pairs'][0]
    chain_id = pair['chainId']
    dex_id = pair['dexId']
    url = pair['url']
    pair_address = pair['pairAddress']
    labels = ','.join(pair['labels'])
    base_token_address = pair['baseToken']['address']
    base_token_name = pair['baseToken']['name']
    base_token_symbol = pair['baseToken']['symbol']
    quote_token_address = pair['quoteToken']['address']
    quote_token_name = pair['quoteToken']['name']
    quote_token_symbol = pair['quoteToken']['symbol']
    price_native = pair['priceNative']
    price_usd = pair['priceUsd']
    h1_buys = pair['txns']['h1']['buys']
    h1_sells = pair['txns']['h1']['sells']
    h24_buys = pair['txns']['h24']['buys']
    h24_sells = pair['txns']['h24']['sells']
    h6_buys = pair['txns']['h6']['buys']
    h6_sells = pair['txns']['h6']['sells']
    m5_buys = pair['txns']['m5']['buys']
    m5_sells = pair['txns']['m5']['sells']
    h24_volume = pair['volume']['h24']
    h6_volume = pair['volume']['h6']
    h1_volume = pair['volume']['h1']
    m5_volume = pair['volume']['m5']
    h1_price_change = pair['priceChange']['h1']
    h24_price_change = pair['priceChange']['h24']
    h6_price_change = pair['priceChange']['h6']
    m5_price_change = pair['priceChange']['m5']
    usd_liquidity = pair['liquidity']['usd']
    base_liquidity = pair['liquidity']['base']
    quote_liquidity = pair['liquidity']['quote']
    fdv = pair['fdv']
    pair_created_at = pair['pairCreatedAt']

    # Connect to the MySQL database
    cnx = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='apoapsis'
    )
    cursor = cnx.cursor()

    # Define the dictionary and extract the relevant values
    # (same as in the previous example)

    # Prepare the SQL statement
    query = '''
    INSERT INTO calls (
        channel_name,
        chain_id,
        dex_id,
        url,
        pair_address,
        labels,
        base_token_address,
        base_token_name,
        base_token_symbol,
        quote_token_address,
        quote_token_name,
        quote_token_symbol,
        price_native,
        price_usd,
        h1_buys,
        h1_sells,
        h24_buys,
        h24_sells,
        h6_buys,
        h6_sells,
        m5_buys,
        m5_sells,
        h24_volume,
        h6_volume,
        h1_volume,
        m5_volume,
        h1_price_change,
        h24_price_change,
        h6_price_change,
        m5_price_change,
        usd_liquidity,
        base_liquidity,
        quote_liquidity,
        fdv,
        pair_created_at,
        calltime
    ) VALUES (
        %(channel_name)s,
        %(chain_id)s,
        %(dex_id)s,
        %(url)s,
        %(pair_address)s,
        %(labels)s,
        %(base_token_address)s,
        %(base_token_name)s,
        %(base_token_symbol)s,
        %(quote_token_address)s,
        %(quote_token_name)s,
        %(quote_token_symbol)s,
        %(price_native)s,
        %(price_usd)s,
        %(h1_buys)s,
        %(h1_sells)s,
        %(h24_buys)s,
        %(h24_sells)s,
        %(h6_buys)s,
        %(h6_sells)s,
        %(m5_buys)s,
        %(m5_sells)s,
        %(h24_volume)s,
        %(h6_volume)s,
        %(h1_volume)s,
        %(m5_volume)s,
        %(h1_price_change)s,
        %(h24_price_change)s,
        %(h6_price_change)s,
        %(m5_price_change)s,
        %(usd_liquidity)s,
        %(base_liquidity)s,
        %(quote_liquidity)s,
        %(fdv)s,
        %(pair_created_at)s,
        %(calltime)s
    )
    '''

    values = {
        'channel_name': channel_name,
        'chain_id': pair['chainId'],
        'dex_id': pair['dexId'],
        'url': pair['url'],
        'pair_address': pair['pairAddress'],
        'labels': ','.join(pair['labels']),
        'base_token_address': pair['baseToken']['address'],
        'base_token_name': pair['baseToken']['name'],
        'base_token_symbol': pair['baseToken']['symbol'],
        'quote_token_address': pair['quoteToken']['address'],
        'quote_token_name': pair['quoteToken']['name'],
        'quote_token_symbol': pair['quoteToken']['symbol'],
        'price_native': pair['priceNative'],
        'price_usd': pair['priceUsd'],
        'h1_buys': pair['txns']['h1']['buys'],
        'h1_sells': pair['txns']['h1']['sells'],
        'h24_buys': pair['txns']['h24']['buys'],
        'h24_sells': pair['txns']['h24']['sells'],
        'h6_buys': pair['txns']['h6']['buys'],
        'h6_sells': pair['txns']['h6']['sells'],
        'm5_buys': pair['txns']['m5']['buys'],
        'm5_sells': pair['txns']['m5']['sells'],
        'h24_volume': pair['volume']['h24'],
        'h6_volume': pair['volume']['h6'],
        'h1_volume': pair['volume']['h1'],
        'm5_volume': pair['volume']['m5'],
        'h1_price_change': pair['priceChange']['h1'],
        'h24_price_change': pair['priceChange']['h24'],
        'h6_price_change': pair['priceChange']['h6'],
        'm5_price_change': pair['priceChange']['m5'],
        'usd_liquidity': pair['liquidity']['usd'],
        'base_liquidity': pair['liquidity']['base'],
        'quote_liquidity': pair['liquidity']['quote'],
        'fdv': pair['fdv'],
        'pair_created_at': pair['pairCreatedAt'],
        'calltime': calltime

    }

    # Execute the SQL query
    cursor.execute(query, values)

    # Commit the changes to the database
    cnx.commit()

    # Close the cursor and database connection
    cursor.close()
    cnx.close()
