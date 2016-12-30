#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import MySQLdb

CONN = MySQLdb.connect('192.168.1.206', 'admin', 'dianjingliuwei101', 'djcourse', charset='utf8')
CUR = CONN.cursor()
DAY = time.strftime('%a')

sql = {
    'Mon':"UPDATE djsh_goods SET pay_num = pay_num + FLOOR(5 + (RAND() * 20)) WHERE store_id IS NULL AND  cat_id IN (SELECT cat_id FROM djsh_cat WHERE cat_name IN ('劳动合同','买卖合同','项目合作','众筹协议','采访合同','文化传媒','居间行纪','购房合同','一般委托代理','基金委托','信托委托','众筹委托','保险代理','招商代理','外贸代理','网络代理','其他代理') AND cat_grade = 4);",
    'Tue':"UPDATE djsh_goods SET pay_num = pay_num + FLOOR(5 + (RAND() * 20)) WHERE store_id IS NULL AND   cat_id IN(SELECT cat_id FROM djsh_cat WHERE cat_name IN('建设工程','股权激励','法律服务','保密协议','财经公关','定向认购','私募基金','定向增发','承销协议','保荐协议','定向资产管理','证券交易','证券上市','证券投资咨询','信托基金','证券委托理财','外汇交易','其他投资理财','股权融资','融资服务','其他融资合同','资产重组','企业重组','股权重组','股权转让','股份代持') AND cat_grade = 4) ;",
    'Wed':"UPDATE djsh_goods SET pay_num = pay_num + FLOOR(5 + (RAND() * 20)) WHERE store_id IS NULL AND  cat_id IN(SELECT cat_id FROM djsh_cat WHERE cat_name IN('公司分立','增资扩股','债权转股权','债务重组','重整和解清算','股权回购','资产转让收购','企业改制','资产管理','对赌协议','风险投资','服务合同','矿业合同','新能源合同','合同能源管理','信用证合同','票据业务','存款合同','还款合同','缴款合同','借款合同','开户合同','清算合同','网上银行合同','其他银>行业务')  AND cat_grade = 4);",
    'Thu':"UPDATE djsh_goods SET pay_num = pay_num + FLOOR(5 + (RAND() * 20)) WHERE store_id IS NULL AND  cat_id IN(SELECT cat_id FROM djsh_cat WHERE cat_name IN('保证合同','质押合同','其他担保','定金合同','抵押合同','>留置合同','婚姻家事','身份关系','公司（企业）设立','股东出资','企业法律风险','农村土地','软件合同','硬件合同','网络合同','主机托管合同','其他合同','房产合同','商业地产','供电合同','供气合同','供热合同','供水合同','其他合同','办学合同','>招生合同') AND cat_grade = 4);",
    'Fri':"UPDATE djsh_goods SET pay_num = pay_num + FLOOR(5 + (RAND() * 20)) WHERE store_id IS NULL AND  cat_id IN(SELECT cat_id FROM djsh_cat WHERE cat_name IN('出国留学','教师聘用合同','就业及就业保障','培养进修','技术合同','一般医疗服务','设计合同','加工承揽','赠与典当','拆迁合同','承包合同','合伙合同','合资合作','联营合同','用地合同','保险合同','企业并购','加盟合同','物流合同','电子商务','小贷公司','期货合同','涉外合同','仓储合同','运输合同','债权转让','拍卖合同') AND cat_grade = 4);",
}

def mysql(sql):
    affect_number = CUR.execute('%s' %sql)
    CUR.close()
    #print affect_number

mysql(sql[DAY])
