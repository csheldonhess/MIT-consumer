from __future__ import unicode_literals

from scrapi.base import OAIHarvester


mit = OAIHarvester(
    name='mit',
    base_url='http://dspace.mit.edu/oai/request',
    property_list=['type', 'source', 'publisher',
                   'format', 'rights', 'identifier',
                   'relation', 'language', 'date'],
    approved_sets=[
        'hdl_1721.1_18193',
        'hdl_1721.1_18194',
        'hdl_1721.1_18195',
        'hdl_1721.1_89012',
        'hdl_1721.1_3650',
        'hdl_1721.1_67473',
        'hdl_1721.1_7630',
        'hdl_1721.1_7760',
        'hdl_1721.1_7744',
        'hdl_1721.1_7768',
        'hdl_1721.1_7767',
        'hdl_1721.1_7631',
        'hdl_1721.1_7766',
        'hdl_1721.1_7632',
        'hdl_1721.1_50867',
        'hdl_1721.1_37333',
        'hdl_1721.1_37334',
        'hdl_1721.1_5460',
        'hdl_1721.1_5461',
        'hdl_1721.1_39813',
        'hdl_1721.1_7771',
        'hdl_1721.1_7634',
        'hdl_1721.1_7635',
        'hdl_1721.1_7772',
        'hdl_1721.1_7633',
        'hdl_1721.1_7765',
        'hdl_1721.1_79695',
        'hdl_1721.1_18236',
        'hdl_1721.1_18237',
        'hdl_1721.1_18238',
        'hdl_1721.1_7626',
        'hdl_1721.1_7755',
        'hdl_1721.1_7770',
        'hdl_1721.1_7627',
        'hdl_1721.1_7756',
        'hdl_1721.1_7628',
        'hdl_1721.1_7629',
        'hdl_1721.1_7769',
        'hdl_1721.1_7784',
        'hdl_1721.1_7636',
        'hdl_1721.1_7591',
        'hdl_1721.1_7785',
        'hdl_1721.1_7592',
        'hdl_1721.1_7783',
        'hdl_1721.1_7352',
        'hdl_1721.1_7780',
        'hdl_1721.1_7637',
        'hdl_1721.1_7781',
        'hdl_1721.1_7638',
        'hdl_1721.1_7639',
        'hdl_1721.1_7779',
        'hdl_1721.1_88072',
        'hdl_1721.1_81425',
        'hdl_1721.1_5462',
        'hdl_1721.1_88531',
        'hdl_1721.1_35731',
        'hdl_1721.1_7641',
        'hdl_1721.1_7789',
        'hdl_1721.1_7791',
        'hdl_1721.1_7643',
        'hdl_1721.1_7642',
        'hdl_1721.1_7790',
        'hdl_1721.1_7640',
        'hdl_1721.1_7788',
        'hdl_1721.1_7644',
        'hdl_1721.1_7795',
        'hdl_1721.1_7645',
        'hdl_1721.1_7796',
        'hdl_1721.1_7646',
        'hdl_1721.1_7794',
        'hdl_1721.1_88516',
        'hdl_1721.1_7934',
        'hdl_1721.1_7648',
        'hdl_1721.1_7800',
        'hdl_1721.1_7801',
        'hdl_1721.1_7649',
        'hdl_1721.1_7652',
        'hdl_1721.1_7802',
        'hdl_1721.1_7653',
        'hdl_1721.1_7799',
        'hdl_1721.1_18186',
        'hdl_1721.1_39096',
        'hdl_1721.1_39099',
        'hdl_1721.1_39100',
        'hdl_1721.1_39097',
        'hdl_1721.1_72924',
        'hdl_1721.1_72923',
        'hdl_1721.1_54823',
        'hdl_1721.1_54828',
        'hdl_1721.1_35730',
        'hdl_1721.1_35732',
        'hdl_1721.1_39117',
        'hdl_1721.1_39115',
        'hdl_1721.1_3651',
        'hdl_1721.1_85979',
        'hdl_1721.1_88006',
        'hdl_1721.1_1779',
        'hdl_1721.1_29807',
        'hdl_1721.1_29808',
        'hdl_1721.1_1778',
        'hdl_1721.1_18187',
        'hdl_1721.1_55346',
        'hdl_1721.1_55382',
        'hdl_1721.1_71743',
        'hdl_1721.1_55383',
        'hdl_1721.1_88179',
        'hdl_1721.1_1780',
        'hdl_1721.1_3765',
        'hdl_1721.1_30597',
        'hdl_1721.1_41529',
        'hdl_1721.1_7806',
        'hdl_1721.1_7655',
        'hdl_1721.1_7807',
        'hdl_1721.1_7656',
        'hdl_1721.1_7654',
        'hdl_1721.1_7805',
        'hdl_1721.1_7657',
        'hdl_1721.1_7811',
        'hdl_1721.1_7658',
        'hdl_1721.1_7812',
        'hdl_1721.1_7810',
        'hdl_1721.1_7659',
        'hdl_1721.1_83579',
        'hdl_1721.1_3766',
        'hdl_1721.1_7816',
        'hdl_1721.1_7661',
        'hdl_1721.1_7818',
        'hdl_1721.1_7662',
        'hdl_1721.1_7663',
        'hdl_1721.1_7817',
        'hdl_1721.1_7660',
        'hdl_1721.1_7815',
        'hdl_1721.1_7886',
        'hdl_1721.1_7709',
        'hdl_1721.1_7711',
        'hdl_1721.1_7887',
        'hdl_1721.1_7710',
        'hdl_1721.1_7888',
        'hdl_1721.1_7885',
        'hdl_1721.1_7708',
        'hdl_1721.1_67705',
        'hdl_1721.1_83560',
        'hdl_1721.1_67903',
        'hdl_1721.1_1781',
        'hdl_1721.1_68162',
        'hdl_1721.1_34284',
        'hdl_1721.1_34283',
        'hdl_1721.1_46718',
        'hdl_1721.1_79432',
        'hdl_1721.1_7714',
        'hdl_1721.1_7892',
        'hdl_1721.1_7893',
        'hdl_1721.1_7715',
        'hdl_1721.1_7891',
        'hdl_1721.1_7712',
        'hdl_1721.1_61396',
        'hdl_1721.1_3652',
        'hdl_1721.1_5551',
        'hdl_1721.1_6750',
        'hdl_1721.1_6751',
        'hdl_1721.1_7624',
        'hdl_1721.1_33950',
        'hdl_1721.1_7666',
        'hdl_1721.1_7822',
        'hdl_1721.1_7667',
        'hdl_1721.1_7823',
        'hdl_1721.1_7821',
        'hdl_1721.1_7665',
        'hdl_1721.1_34286',
        'hdl_1721.1_34285',
        'hdl_1721.1_3767',
        'hdl_1721.1_3768',
        'hdl_1721.1_3769',
        'hdl_1721.1_3653',
        'hdl_1721.1_7671',
        'hdl_1721.1_7827',
        'hdl_1721.1_7828',
        'hdl_1721.1_7672',
        'hdl_1721.1_7826',
        'hdl_1721.1_7670',
        'hdl_1721.1_1782',
        'hdl_1721.1_3550',
        'hdl_1721.1_7353',
        'hdl_1721.1_39119',
        'hdl_1721.1_1784',
        'hdl_1721.1_29811',
        'hdl_1721.1_29812',
        'hdl_1721.1_55347',
        'hdl_1721.1_1785',
        'hdl_1721.1_1786',
        'hdl_1721.1_88005',
        'hdl_1721.1_60280',
        'hdl_1721.1_1783',
        'hdl_1721.1_7833',
        'hdl_1721.1_7674',
        'hdl_1721.1_7834',
        'hdl_1721.1_7675',
        'hdl_1721.1_7832',
        'hdl_1721.1_7673',
        'hdl_1721.1_29814',
        'hdl_1721.1_7729',
        'hdl_1721.1_7918',
        'hdl_1721.1_7730',
        'hdl_1721.1_7919',
        'hdl_1721.1_7917',
        'hdl_1721.1_7728',
        'hdl_1721.1_35733',
        'hdl_1721.1_29796',
        'hdl_1721.1_7509',
        'hdl_1721.1_7678',
        'hdl_1721.1_7838',
        'hdl_1721.1_7839',
        'hdl_1721.1_7679',
        'hdl_1721.1_7840',
        'hdl_1721.1_7677',
        'hdl_1721.1_7676',
        'hdl_1721.1_7837',
        'hdl_1721.1_1788',
        'hdl_1721.1_7844',
        'hdl_1721.1_7681',
        'hdl_1721.1_7682',
        'hdl_1721.1_7845',
        'hdl_1721.1_7680',
        'hdl_1721.1_7843',
        'hdl_1721.1_37287',
        'hdl_1721.1_7849',
        'hdl_1721.1_7686',
        'hdl_1721.1_7685',
        'hdl_1721.1_7851',
        'hdl_1721.1_7684',
        'hdl_1721.1_7850',
        'hdl_1721.1_7848',
        'hdl_1721.1_7683',
        'hdl_1721.1_7717',
        'hdl_1721.1_7899',
        'hdl_1721.1_7900',
        'hdl_1721.1_7718',
        'hdl_1721.1_7716',
        'hdl_1721.1_7898',
        'hdl_1721.1_81436',
        'hdl_1721.1_63243',
        'hdl_1721.1_7532',
        'hdl_1721.1_18116',
        'hdl_1721.1_49433',
        'hdl_1721.1_1787',
        'hdl_1721.1_5539',
        'hdl_1721.1_7295',
        'hdl_1721.1_7296',
        'hdl_1721.1_3654',
        'hdl_1721.1_18239',
        'hdl_1721.1_88182',
        'hdl_1721.1_88019',
        'hdl_1721.1_83516',
        'hdl_1721.1_76749',
        'hdl_1721.1_67476',
        'hdl_1721.1_7855',
        'hdl_1721.1_7688',
        'hdl_1721.1_7857',
        'hdl_1721.1_7690',
        'hdl_1721.1_7689',
        'hdl_1721.1_7856',
        'hdl_1721.1_7687',
        'hdl_1721.1_7854',
        'hdl_1721.1_67474',
        'hdl_1721.1_67477',
        'hdl_1721.1_67475',
        'hdl_1721.1_7692',
        'hdl_1721.1_7861',
        'hdl_1721.1_1789',
        'hdl_1721.1_7863',
        'hdl_1721.1_7694',
        'hdl_1721.1_7693',
        'hdl_1721.1_7862',
        'hdl_1721.1_7691',
        'hdl_1721.1_7860',
        'hdl_1721.1_7904',
        'hdl_1721.1_7721',
        'hdl_1721.1_5067',
        'hdl_1721.1_7720',
        'hdl_1721.1_7905',
        'hdl_1721.1_7719',
        'hdl_1721.1_7903',
        'hdl_1721.1_3774',
        'hdl_1721.1_7356',
        'hdl_1721.1_7357',
        'hdl_1721.1_85978',
        'hdl_1721.1_16560',
        'hdl_1721.1_16547',
        'hdl_1721.1_16556',
        'hdl_1721.1_16552',
        'hdl_1721.1_16564',
        'hdl_1721.1_7696',
        'hdl_1721.1_7867',
        'hdl_1721.1_7868',
        'hdl_1721.1_7697',
        'hdl_1721.1_7866',
        'hdl_1721.1_7695',
        'hdl_1721.1_3770',
        'hdl_1721.1_32548',
        'hdl_1721.1_7871',
        'hdl_1721.1_7700',
        'hdl_1721.1_7699',
        'hdl_1721.1_7872',
        'hdl_1721.1_7870',
        'hdl_1721.1_7698',
        'hdl_1721.1_89476',
        'hdl_1721.1_88073',
        'hdl_1721.1_80741',
        'hdl_1721.1_16553',
        'hdl_1721.1_16548',
        'hdl_1721.1_16557',
        'hdl_1721.1_16565',
        'hdl_1721.1_16561',
        'hdl_1721.1_80814',
        'hdl_1721.1_88074',
        'hdl_1721.1_54831',
        'hdl_1721.1_54825',
        'hdl_1721.1_39103',
        'hdl_1721.1_39111',
        'hdl_1721.1_39112',
        'hdl_1721.1_39104',
        'hdl_1721.1_1790',
        'hdl_1721.1_1791',
        'hdl_1721.1_5435',
        'hdl_1721.1_55385',
        'hdl_1721.1_18157',
        'hdl_1721.1_86180',
        'hdl_1721.1_26678',
        'hdl_1721.1_18165',
        'hdl_1721.1_30600',
        'hdl_1721.1_18163',
        'hdl_1721.1_18228',
        'hdl_1721.1_26584',
        'hdl_1721.1_26672',
        'hdl_1721.1_18161',
        'hdl_1721.1_18217',
        'hdl_1721.1_26399',
        'hdl_1721.1_18213',
        'hdl_1721.1_26401',
        'hdl_1721.1_18155',
        'hdl_1721.1_18159',
        'hdl_1721.1_18897',
        'hdl_1721.1_45562',
        'hdl_1721.1_5436',
        'hdl_1721.1_5529',
        'hdl_1721.1_5530',
        'hdl_1721.1_32529',
        'hdl_1721.1_18111',
        'hdl_1721.1_5531',
        'hdl_1721.1_18107',
        'hdl_1721.1_18168',
        'hdl_1721.1_5444',
        'hdl_1721.1_5443',
        'hdl_1721.1_18105',
        'hdl_1721.1_18109',
        'hdl_1721.1_34016',
        'hdl_1721.1_62236',
        'hdl_1721.1_5437',
        'hdl_1721.1_18078',
        'hdl_1721.1_18076',
        'hdl_1721.1_18169',
        'hdl_1721.1_18080',
        'hdl_1721.1_18106',
        'hdl_1721.1_18108',
        'hdl_1721.1_18110',
        'hdl_1721.1_18112',
        'hdl_1721.1_32530',
        'hdl_1721.1_18079',
        'hdl_1721.1_18077',
        'hdl_1721.1_70033',
        'hdl_1721.1_67478',
        'hdl_1721.1_16558',
        'hdl_1721.1_16554',
        'hdl_1721.1_16546',
        'hdl_1721.1_16562',
        'hdl_1721.1_16550',
        'hdl_1721.1_83528',
        'hdl_1721.1_88075',
        'hdl_1721.1_43714',
        'hdl_1721.1_88076',
        'hdl_1721.1_83613',
        'hdl_1721.1_41896',
        'hdl_1721.1_88000',
        'hdl_1721.1_18216',
        'hdl_1721.1_18212',
        'hdl_1721.1_18227',
        'hdl_1721.1_26677',
        'hdl_1721.1_26583',
        'hdl_1721.1_26673',
        'hdl_1721.1_18892',
        'hdl_1721.1_87999',
        'hdl_1721.1_49817',
        'hdl_1721.1_49830',
        'hdl_1721.1_50644',
        'hdl_1721.1_50655',
        'hdl_1721.1_50666',
        'hdl_1721.1_50676',
        'hdl_1721.1_50686',
        'hdl_1721.1_50716',
        'hdl_1721.1_50726',
        'hdl_1721.1_50740',
        'hdl_1721.1_50761',
        'hdl_1721.1_50763',
        'hdl_1721.1_50793',
        'hdl_1721.1_50794',
        'hdl_1721.1_50823',
        'hdl_1721.1_50838',
        'hdl_1721.1_50852',
        'hdl_1721.1_50869',
        'hdl_1721.1_50883',
        'hdl_1721.1_50898',
        'hdl_1721.1_50913',
        'hdl_1721.1_50914',
        'hdl_1721.1_50915',
        'hdl_1721.1_50916',
        'hdl_1721.1_50917',
        'hdl_1721.1_51010',
        'hdl_1721.1_51011',
        'hdl_1721.1_51073',
        'hdl_1721.1_51074',
        'hdl_1721.1_51075',
        'hdl_1721.1_51122',
        'hdl_1721.1_51138',
        'hdl_1721.1_51139',
        'hdl_1721.1_51189',
        'hdl_1721.1_51190',
        'hdl_1721.1_51236',
        'hdl_1721.1_51237',
        'hdl_1721.1_51238',
        'hdl_1721.1_51239',
        'hdl_1721.1_51900',
        'hdl_1721.1_51928',
        'hdl_1721.1_51952',
        'hdl_1721.1_51976',
        'hdl_1721.1_52013',
        'hdl_1721.1_52041',
        'hdl_1721.1_52068',
        'hdl_1721.1_52095',
        'hdl_1721.1_52117',
        'hdl_1721.1_52145',
        'hdl_1721.1_52168',
        'hdl_1721.1_52189',
        'hdl_1721.1_52212',
        'hdl_1721.1_52245',
        'hdl_1721.1_52274',
        'hdl_1721.1_53335',
        'hdl_1721.1_53355',
        'hdl_1721.1_53386',
        'hdl_1721.1_53418',
        'hdl_1721.1_53448',
        'hdl_1721.1_53474',
        'hdl_1721.1_53510',
        'hdl_1721.1_53587',
        'hdl_1721.1_53612',
        'hdl_1721.1_53635',
        'hdl_1721.1_53674',
        'hdl_1721.1_53751',
        'hdl_1721.1_53779',
        'hdl_1721.1_53806',
        'hdl_1721.1_53845',
        'hdl_1721.1_53869',
        'hdl_1721.1_53899',
        'hdl_1721.1_53923',
        'hdl_1721.1_53955',
        'hdl_1721.1_53988',
        'hdl_1721.1_54016',
        'hdl_1721.1_54038',
        'hdl_1721.1_55589',
        'hdl_1721.1_54105',
        'hdl_1721.1_54130',
        'hdl_1721.1_54154',
        'hdl_1721.1_55434',
        'hdl_1721.1_55460',
        'hdl_1721.1_55490',
        'hdl_1721.1_55512',
        'hdl_1721.1_55553',
        'hdl_1721.1_55617',
        'hdl_1721.1_55651',
        'hdl_1721.1_55672',
        'hdl_1721.1_55714',
        'hdl_1721.1_55747',
        'hdl_1721.1_55775',
        'hdl_1721.1_55817',
        'hdl_1721.1_55852',
        'hdl_1721.1_55870',
        'hdl_1721.1_56010',
        'hdl_1721.1_56030',
        'hdl_1721.1_56066',
        'hdl_1721.1_56089',
        'hdl_1721.1_56109',
        'hdl_1721.1_56128',
        'hdl_1721.1_56161',
        'hdl_1721.1_56182',
        'hdl_1721.1_56201',
        'hdl_1721.1_56220',
        'hdl_1721.1_56265',
        'hdl_1721.1_56266',
        'hdl_1721.1_56267',
        'hdl_1721.1_56345',
        'hdl_1721.1_56375',
        'hdl_1721.1_56393',
        'hdl_1721.1_56412',
        'hdl_1721.1_56431',
        'hdl_1721.1_56458',
        'hdl_1721.1_56479',
        'hdl_1721.1_56505',
        'hdl_1721.1_56533',
        'hdl_1721.1_56582',
        'hdl_1721.1_56610',
        'hdl_1721.1_56635',
        'hdl_1721.1_56676',
        'hdl_1721.1_56715',
        'hdl_1721.1_56751',
        'hdl_1721.1_56746',
        'hdl_1721.1_56732',
        'hdl_1721.1_56717',
        'hdl_1721.1_56716',
        'hdl_1721.1_56714',
        'hdl_1721.1_56708',
        'hdl_1721.1_56692',
        'hdl_1721.1_56679',
        'hdl_1721.1_56678',
        'hdl_1721.1_56675',
        'hdl_1721.1_56674',
        'hdl_1721.1_56673',
        'hdl_1721.1_56672',
        'hdl_1721.1_56661',
        'hdl_1721.1_56647',
        'hdl_1721.1_56644',
        'hdl_1721.1_56638',
        'hdl_1721.1_56637',
        'hdl_1721.1_4059',
        'hdl_1721.1_5552',
        'hdl_1721.1_7727',
        'hdl_1721.1_7726',
        'hdl_1721.1_7725',
        'hdl_1721.1_7914',
        'hdl_1721.1_7915',
        'hdl_1721.1_7913',
        'hdl_1721.1_46333',
        'hdl_1721.1_76637',
        'hdl_1721.1_46704',
        'hdl_1721.1_85574',
        'hdl_1721.1_62800',
        'hdl_1721.1_65423',
        'hdl_1721.1_40283',
        'hdl_1721.1_16551',
        'hdl_1721.1_16545',
        'hdl_1721.1_16555',
        'hdl_1721.1_16559',
        'hdl_1721.1_16563',
        'hdl_1721.1_70040',
        'hdl_1721.1_37288',
        'hdl_1721.1_1792',
        'hdl_1721.1_18188',
        'hdl_1721.1_53733',
        'hdl_1721.1_76638',
        'hdl_1721.1_88003',
        'hdl_1721.1_7923',
        'hdl_1721.1_7740',
        'hdl_1721.1_7739',
        'hdl_1721.1_7924',
        'hdl_1721.1_7922',
        'hdl_1721.1_7738',
        'hdl_1721.1_87998',
        'hdl_1721.1_65424',
        'hdl_1721.1_76639',
        'hdl_1721.1_29797',
        'hdl_1721.1_76745',
        'hdl_1721.1_1793',
        'hdl_1721.1_7743',
        'hdl_1721.1_7928',
        'hdl_1721.1_7742',
        'hdl_1721.1_7929',
        'hdl_1721.1_7927',
        'hdl_1721.1_7741',
        'hdl_1721.1_55584',
        'hdl_1721.1_55916',
        'hdl_1721.1_42001',
        'hdl_1721.1_26585',
        'hdl_1721.1_29798',
        'hdl_1721.1_18230',
        'hdl_1721.1_18899',
        'hdl_1721.1_26674',
        'hdl_1721.1_18219',
        'hdl_1721.1_18215',
        'hdl_1721.1_26680',
        'hdl_1721.1_80739',
        'hdl_1721.1_80746',
        'hdl_1721.1_88077',
        'hdl_1721.1_18235',
        'hdl_1721.1_18225',
        'hdl_1721.1_18224',
        'hdl_1721.1_55586',
        'hdl_1721.1_55719',
        'hdl_1721.1_55588',
        'hdl_1721.1_78860',
        'hdl_1721.1_18226',
        'hdl_1721.1_7703',
        'hdl_1721.1_7876',
        'hdl_1721.1_7877',
        'hdl_1721.1_7704',
        'hdl_1721.1_7702',
        'hdl_1721.1_7875',
        'hdl_1721.1_16459',
        'hdl_1721.1_18240',
        'hdl_1721.1_7358',
        'hdl_1721.1_3771',
        'hdl_1721.1_33228',
        'hdl_1721.1_18229',
        'hdl_1721.1_26679',
        'hdl_1721.1_80740',
        'hdl_1721.1_18898',
        'hdl_1721.1_26676',
        'hdl_1721.1_18218',
        'hdl_1721.1_26586',
        'hdl_1721.1_18222',
        'hdl_1721.1_88078',
        'hdl_1721.1_34010',
        'hdl_1721.1_18214',
        'hdl_1721.1_81470',
        'hdl_1721.1_88079',
        'hdl_1721.1_83431',
        'hdl_1721.1_52116',
        'hdl_1721.1_39118',
        'hdl_1721.1_89011',
        'hdl_1721.1_50866',
        'hdl_1721.1_37332',
        'hdl_1721.1_34280',
        'hdl_1721.1_5459',
        'hdl_1721.1_16538',
        'hdl_1721.1_55583',
        'hdl_1721.1_87997',
        'hdl_1721.1_88181',
        'hdl_1721.1_16539',
        'hdl_1721.1_7752',
        'hdl_1721.1_40282',
        'hdl_1721.1_67472',
        'hdl_1721.1_88529',
        'hdl_1721.1_34009',
        'hdl_1721.1_3549',
        'hdl_1721.1_55585',
        'hdl_1721.1_3764',
        'hdl_1721.1_7530',
        'hdl_1721.1_18211',
        'hdl_1721.1_16165',
        'hdl_1721.1_18154',
        'hdl_1721.1_26400',
        'hdl_1721.1_18203',
        'hdl_1721.1_39094',
        'hdl_1721.1_54826',
        'hdl_1721.1_33227',
        'hdl_1721.1_5458',
        'hdl_1721.1_16540',
        'hdl_1721.1_88071',
        'hdl_1721.1_16535',
        'hdl_1721.1_29806',
        'hdl_1721.1_18118',
        'hdl_1721.1_55384',
        'hdl_1721.1_18160',
        'hdl_1721.1_85573',
        'hdl_1721.1_7758',
        'hdl_1721.1_7749',
        'hdl_1721.1_7761',
        'hdl_1721.1_7776',
        'hdl_1721.1_7786',
        'hdl_1721.1_7792',
        'hdl_1721.1_7797',
        'hdl_1721.1_7803',
        'hdl_1721.1_7808',
        'hdl_1721.1_7813',
        'hdl_1721.1_7819',
        'hdl_1721.1_7824',
        'hdl_1721.1_7829',
        'hdl_1721.1_7835',
        'hdl_1721.1_7841',
        'hdl_1721.1_7846',
        'hdl_1721.1_7852',
        'hdl_1721.1_1774',
        'hdl_1721.1_7864',
        'hdl_1721.1_5427',
        'hdl_1721.1_7873',
        'hdl_1721.1_67704',
        'hdl_1721.1_7883',
        'hdl_1721.1_18204',
        'hdl_1721.1_30596',
        'hdl_1721.1_46702',
        'hdl_1721.1_7507',
        'hdl_1721.1_18202',
        'hdl_1721.1_67902',
        'hdl_1721.1_68161',
        'hdl_1721.1_55718',
        'hdl_1721.1_55915',
        'hdl_1721.1_34282',
        'hdl_1721.1_76636',
        'hdl_1721.1_7889',
        'hdl_1721.1_6749',
        'hdl_1721.1_79431',
        'hdl_1721.1_61395',
        'hdl_1721.1_7932',
        'hdl_1721.1_18205',
        'hdl_1721.1_46717',
        'hdl_1721.1_55587',
        'hdl_1721.1_34281',
        'hdl_1721.1_18206',
        'hdl_1721.1_26398',
        'hdl_1721.1_18192',
        'hdl_1721.1_1775',
        'hdl_1721.1_70032',
        'hdl_1721.1_29810',
        'hdl_1721.1_80738',
        'hdl_1721.1_88180',
        'hdl_1721.1_29795',
        'hdl_1721.1_18162',
        'hdl_1721.1_68160',
        'hdl_1721.1_7896',
        'hdl_1721.1_18156',
        'hdl_1721.1_41894',
        'hdl_1721.1_7531',
        'hdl_1721.1_7581',
        'hdl_1721.1_33971',
        'hdl_1721.1_49432',
        'hdl_1721.1_33970',
        'hdl_1721.1_1776',
        'hdl_1721.1_1773',
        'hdl_1721.1_7582',
        'hdl_1721.1_7294',
        'hdl_1721.1_18158',
        'hdl_1721.1_30599',
        'hdl_1721.1_88018',
        'hdl_1721.1_7351',
        'hdl_1721.1_70038',
        'hdl_1721.1_5066',
        'hdl_1721.1_16537',
        'hdl_1721.1_7933',
        'hdl_1721.1_18167',
        'hdl_1721.1_53732',
        'hdl_1721.1_41528',
        'hdl_1721.1_88004',
        'hdl_1721.1_54829',
        'hdl_1721.1_39101',
        'hdl_1721.1_32547',
        'hdl_1721.1_80743',
        'hdl_1721.1_29813',
        'hdl_1721.1_80745',
        'hdl_1721.1_88530',
        'hdl_1721.1_18119',
        'hdl_1721.1_16536',
        'hdl_1721.1_62799',
        'hdl_1721.1_18170',
        'hdl_1721.1_4058',
        'hdl_1721.1_88001',
        'hdl_1721.1_49816',
        'hdl_1721.1_62234',
        'hdl_1721.1_7508',
        'hdl_1721.1_33226',
        'hdl_1721.1_7911',
        'hdl_1721.1_46703',
        'hdl_1721.1_18164',
        'hdl_1721.1_3649',
        'hdl_1721.1_1777',
        'hdl_1721.1_16541',
        'hdl_1721.1_18117',
        'hdl_1721.1_18210',
        'hdl_1721.1_45561',
        'hdl_1721.1_18201',
        'hdl_1721.1_18185',
        'hdl_1721.1_7920',
        'hdl_1721.1_7925',
        'hdl_1721.1_16542',
        'hdl_1721.1_55345',
        'hdl_1721.1_7759',
        'hdl_1721.1_7622',
        'hdl_1721.1_7754',
        'hdl_1721.1_7782',
        'hdl_1721.1_7778',
        'hdl_1721.1_7787',
        'hdl_1721.1_7793',
        'hdl_1721.1_7798',
        'hdl_1721.1_39098',
        'hdl_1721.1_39095',
        'hdl_1721.1_54827',
        'hdl_1721.1_54822',
        'hdl_1721.1_39116',
        'hdl_1721.1_39113',
        'hdl_1721.1_7750',
        'hdl_1721.1_7621',
        'hdl_1721.1_7583',
        'hdl_1721.1_7589',
        'hdl_1721.1_7593',
        'hdl_1721.1_7594',
        'hdl_1721.1_7595',
        'hdl_1721.1_7596',
        'hdl_1721.1_7597',
        'hdl_1721.1_7598',
        'hdl_1721.1_7599',
        'hdl_1721.1_7600',
        'hdl_1721.1_7601',
        'hdl_1721.1_7602',
        'hdl_1721.1_7603',
        'hdl_1721.1_7604',
        'hdl_1721.1_7605',
        'hdl_1721.1_7606',
        'hdl_1721.1_7607',
        'hdl_1721.1_7608',
        'hdl_1721.1_7609',
        'hdl_1721.1_7610',
        'hdl_1721.1_7804',
        'hdl_1721.1_7809',
        'hdl_1721.1_7814',
        'hdl_1721.1_7884',
        'hdl_1721.1_7612',
        'hdl_1721.1_7613',
        'hdl_1721.1_7890',
        'hdl_1721.1_7820',
        'hdl_1721.1_7825',
        'hdl_1721.1_7830',
        'hdl_1721.1_7916',
        'hdl_1721.1_7836',
        'hdl_1721.1_7842',
        'hdl_1721.1_7847',
        'hdl_1721.1_7614',
        'hdl_1721.1_7897',
        'hdl_1721.1_7853',
        'hdl_1721.1_7859',
        'hdl_1721.1_7902',
        'hdl_1721.1_7615',
        'hdl_1721.1_7865',
        'hdl_1721.1_7869',
        'hdl_1721.1_54830',
        'hdl_1721.1_54824',
        'hdl_1721.1_39110',
        'hdl_1721.1_39102',
        'hdl_1721.1_7617',
        'hdl_1721.1_7912',
        'hdl_1721.1_7618',
        'hdl_1721.1_7737',
        'hdl_1721.1_7921',
        'hdl_1721.1_7926',
        'hdl_1721.1_7620',
        'hdl_1721.1_7874',
        'hdl_1721.1_7959',
        'hdl_1721.1_65422',
        'hdl_1721.1_78859',
        'hdl_1721.1_18131',
        'hdl_1721.1_89474',
        'hdl_1721.1_18209',
        'hdl_1721.1_76748',
        'hdl_1721.1_46332',
        'hdl_1721.1_5432',
        'hdl_1721.1_5549',
        'hdl_1721.1_18081',
        'hdl_1721.1_18082',
        'hdl_1721.1_5523',
        'hdl_1721.1_34015',
        'hdl_1721.1_5524',
        'hdl_1721.1_18083',
        'hdl_1721.1_18084',
        'hdl_1721.1_5442',
        'hdl_1721.1_32528',
        'hdl_1721.1_5528',
        'hdl_1721.1_5431'
    ]
)

consume = mit.harvest
normalize = mit.normalize
