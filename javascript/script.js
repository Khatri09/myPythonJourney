[{ begMonth: "08", endMonth: "09" }].forEach((period) => {
    ["HUAWEI_PAY_HCE"].forEach((walletProviderId) => {
        print(`counting active tokens between ${period.begMonth}/22 and ${period.endMonth}/22 for ${walletProviderId}`);

        try {
            const activeTokenCount = db["cards_INTESA_IT1"].aggregate(
                [
                    {
                        '$unwind': {
                            'path': '$virtualCards'
                        }
                    }, {
                        '$match': {
                            '$and': [
                                {
                                    'virtualCards.history.enrollmentDate': {
                                        '$lt': ISODate(`2022-${period.endMonth}-01T00:00:00.000Z`)
                                    }
                                }, {
                                    '$or': [
                                        {
                                            'virtualCards.history.deletionDate': {
                                                '$exists': false
                                            }
                                        }, {
                                            '$and': [
                                                {
                                                    'virtualCards.history.deletionDate': {
                                                        '$gt': ISODate(`2022-${period.begMonth}-01T00:00:00.000Z`)
                                                    }
                                                }, {
                                                    'virtualCards.history.deletionDate': {
                                                        '$lt': ISODate(`2022-${period.endMonth}-01T00:00:00.000Z`)
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    }, {
                        '$count': 'count'
                    }
                ],
                { allowDiskUse: true }
            ).toArray();

            print(`from ${period.begMonth}/22 to ${period.endMonth}/22 ${activeTokenCount[0] ? activeTokenCount[0].count : 0} active tokens for ${walletProviderId}`);
        }

        catch (err) {
            print(err);
        }
    })
})