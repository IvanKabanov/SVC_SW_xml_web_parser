import untangle
from svc_xml_parser import Nd_parser, Nn_parser, Nm_parser, Nv_parser
from db_create import db_session, Nd, Nm

# C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7kupload_id\Nd_stats_78Nupload_idK98-2_upload_id7040upload_id_upload_idupload_id2309

def path_to_file(path_to_file, upload_id):

	obj = untangle.parse(path_to_file)

	contains = obj.diskStatsColl['contains']

	if contains	== 'driveStats':
		res = Nd_parser(path_to_file, upload_id)

		data = res

		# i=0

		for item in res:

			to_database=Nd(idx=item['idx'], ro=item['ro'], rb=item['rb'], wo=item['wo'],
				           re=item['re'], we=item['we'], rq=item['rq'], wq=item['wq'],
				           ure=item['ure'], uwe=item['uwe'], urq=item['urq'], uwq=item['uwq'],
				           pre=item['pre'], pwe=item['pwe'], pro=item['pro'], pwo=item['pwo'],
				           upload_id=item['upload_id'])

			db_session.add(to_database)

			# i += 1
			
		db_session.commit()

	elif contains	== 'managedDiskStats':
		res = Nm_parser(path_to_file, upload_id)

		data = res

		# i=0

		for item in res:

			to_database=Nm(idx=item['idx'], ro=item['ro'], wo=item['wo'], rb=item['rb'],
				           wb=item['wb'], re=item['re'], we=item['we'], rq=item['rq'],
				           wq=item['wq'], ure=item['ure'], uwe=item['uwe'], urq=item['urq'],
				           uwq=item['uwq'], pre=item['pre'], pwe=item['pwe'], pro=item['pro'],
				           pwo=item['pwo'], upload_id=item['upload_id'])

			db_session.add(to_database)

			# i += 1
			
		db_session.commit()

	elif contains	== 'nodeStats':
		res = Nn_parser(path_to_file, upload_id)

	elif contains	== 'virtualDiskStats':
		res = Nv_parser(path_to_file, upload_id)

	else:
		print('Нужных файлов нет')
		return

	#print(contains)
