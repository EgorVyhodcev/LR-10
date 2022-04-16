#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import flights


class FlightsTests(unittest.TestCase):
    def test_select_all_3_rows(self):
        testlist = [
            {
                'flight_destination': 'Hollywood',
                'flight_number': 'HL128',
                'airplane_type': 'Passenger'
            },
            {
                'flight_destination': 'Gtreshd',
                'flight_number': 'GH356',
                'airplane_type': 'Military'
             },
            {
                'flight_destination': 'Yfhdjs',
                'flight_number': 'Y4367',
                'airplane_type': 'Sanitary'
             }
        ]
        self.assertListEqual(flights.select_all('test_flights.db'), testlist)

    def test_select_by_type(self):
        ans = [
            {
                'flight_destination': 'Gtreshd',
                'flight_number': 'GH356',
                'airplane_type': 'Military'
             }
        ]
        self.assertListEqual(
            flights.select_flights('test_flights.db', 'Military'), ans
        )

    def test_select_all_after_adding(self):
        dest = "Miami"
        flight_num = "MI194"
        type = "Passenger"
        flights.add_flight('test_flights.db', dest, flight_num, type)
        testlist = [
            {
                'flight_destination': 'Hollywood',
                'flight_number': 'HL128',
                'airplane_type': 'Passenger'
            },
            {
                'flight_destination': 'Gtreshd',
                 'flight_number': 'GH356',
                 'airplane_type': 'Military'
             },
            {
                'flight_destination': 'Yfhdjs',
                 'flight_number': 'Y4367',
                 'airplane_type': 'Sanitary'
             },
            {
                'flight_destination': 'Miami',
                'flight_number': 'MI194',
                'airplane_type': 'Passenger'
            }
        ]
        self.assertListEqual(flights.select_all('test_flights.db'), testlist)
