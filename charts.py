# Icons classes from https://fontawesome.com/v4/icons/

import json

class Charts:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.charts_data = [
            {
                "Name": "Pie Chart",
                "Description": "A pie chart to show the male to female ratio",
                "Icon_Class": "fas fa-chart-pie", 
                "Chart_Data": self.pie_chart(),
            },
            {
                "Name": "Bar Chart",
                "Description": "A stacked bar chart to show all passengers by age",
                "Icon_Class": "fas fa-chart-bar", 
                "Chart_Data": self.bar_chart(),
            }
        ]
    
    # Reference https://www.highcharts.com/demo/bar-stacked
    def bar_chart(self):
        categories_by_age = [
            'Younger Than 16', 
            'Between 16 and 26', 
            'Between 26 and 36', 
            'Between 36 and 62', 
            'Older than 62'
        ]
            

        return {
            'chart': {
                'type': 'bar'
            },
            'title': {
                'text': 'All Passengers By Age'
            },
            'xAxis': {
                'categories': categories_by_age
            },
            'plotOptions': {
                'series': {
                    'stacking': 'normal'
                }
            },
            'series': [{
                'name': 'Male',
                'data': self.male_female_by_age_group('male')
            }, {
                'name': 'Female',
                'data': self.male_female_by_age_group('female')
            }]
        }

    def male_female_by_age_group(self, sex):
        younger_than_16 = (
            self.data_frame[(self.data_frame.Age <= 16)].Sex == sex
        ).sum()

        between_16_26 = (
            self.data_frame[(self.data_frame.Age > 16) & (self.data_frame.Age <= 26)].Sex == sex
        ).sum()

        between_26_36 = (
            self.data_frame[(self.data_frame.Age > 26) & (self.data_frame.Age <= 36)].Sex == sex
        ).sum()

        between_36_62 = (
            self.data_frame[(self.data_frame.Age > 36) & (self.data_frame.Age <= 62)].Sex == sex
        ).sum()

        older_than_62 = (
            self.data_frame[(self.data_frame.Age > 62)].Sex == sex
        ).sum()

        return [
            int(younger_than_16),
            int(between_16_26),
            int(between_26_36),
            int(between_36_62),
            int(older_than_62)
        ]

    # Reference https://www.highcharts.com/demo/pie-basic
    def pie_chart(self):
        return {
            'chart': {
                'type': 'pie'
            },
            'title': {
                'text': 'Male to Female Ratio'
            },
            'series': [{
                'name': 'Ratio',
                'colorByPoint': 'true',
                'data': [
                    {
                        'name': 'Male',
                        'y': self.find_num_of_male(),
                    },
                    {
                        'name': 'Female',
                        'y': self.find_num_of_female(),
                    }
                ] 
            }]
        } 

    def find_num_of_male(self):
        return int((self.data_frame.Sex == 'male').sum())
    
    def find_num_of_female(self):
        return int((self.data_frame.Sex == 'female').sum())
