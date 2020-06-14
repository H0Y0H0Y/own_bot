from functions.covid_ph.processor import f

# Codes used in the CSV file
CEBU_PROV = "PH0722"
CEBU_CITY = "PH072217000"
MANDAUE_CITY = "PH072230000"
LAPU_LAPU_CITY = "PH072226000"

# values: [City codes for CityMuniPSGC, City name text]
callback_query_dict = {"cc": [CEBU_CITY, 'Cebu City'],
                       "mc": [MANDAUE_CITY, 'Mandaue City'],
                       "llc": [LAPU_LAPU_CITY, 'Lapu-lapu City']}


def handle_get_cases_by_city(bot, query):
    reply_msg = _create_breakdown_of_cases_text(query)
    bot.send_message(query.message.chat.id, reply_msg)


def _create_breakdown_of_cases_text(query):
    city = callback_query_dict.get(query.data)[0]
    city_name = callback_query_dict.get(query.data)[1]
    city_dict = _get_total_cases_by_city(city)
    city_cases = city_dict['city_cases']
    asymptomatic = city_dict['asymptomatic_cases']
    mild = city_dict['mild_cases']
    recovered = city_dict['recovered_cases']
    critical = city_dict['critical_cases']
    died = city_dict['died_cases']
    no_status = city_dict['no_status_cases']

    return f"Total number of cases in {city_name}:\n {city_cases}" \
           f"\nTotal asymptomatic cases: {asymptomatic}" \
           f"\nTotal mild cases: {mild}" \
           f"\nTotal recovered cases: {recovered}" \
           f"\nTotal critical cases: {critical}" \
           f"\nTotal death: {died}" \
           f"\nCases with no status: {no_status}"


def _get_total_cases_by_city(city):
    cases_dict = {}
    dfs = f.csv_data_frame
    city_cases = dfs[dfs['CityMuniPSGC'].str.contains(
                        city, na=False)]
    mild_cases = city_cases[city_cases[
                                    'HealthStatus'] == 'Mild']
    asymptomatic_cases = city_cases[city_cases[
                                    'HealthStatus'] == 'Asymptomatic']
    recovered_cases = city_cases[city_cases[
                                    'HealthStatus'] == 'Recovered']
    critical_cases = city_cases[city_cases[
                                    'HealthStatus'] == 'Critical']
    died_cases = city_cases[city_cases[
                                    'HealthStatus'] == 'Died']
    no_status_cases = city_cases[city_cases[
                                    'HealthStatus'].isnull()]

    cases_dict = {"city_cases": str(city_cases.shape[0]),
                  "mild_cases": str(mild_cases.shape[0]),
                  "asymptomatic_cases": str(asymptomatic_cases.shape[0]),
                  "recovered_cases": str(recovered_cases.shape[0]),
                  "critical_cases": str(critical_cases.shape[0]),
                  "died_cases": str(died_cases.shape[0]),
                  "no_status_cases": str(no_status_cases.shape[0])}
    return cases_dict
