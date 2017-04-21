import untangle
from svc_xml_parser import Nd_parser, Nn_parser, Nm_parser, Nv_parser
from db_insert import path_to_file

path_list = [r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_084425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_085925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_091425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_092925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_094425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_095925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_101425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_102925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_104425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_105925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_111425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_112925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_114424',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_115924',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_121424',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nd_stats_78G0036-1_170401_122924',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_084425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_085925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_091425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_092925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_094425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_095925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_101425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_102925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_104425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_105925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_111425',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_112925',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_114424',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_115924',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_121424',
 			 r'C:\projects\diploma\SVC_SW_xml_web_parser\examples\stats\v7k2\Nm_stats_78G0036-1_170401_122924',]

upload_id = 0

for path in path_list:

	upload_id += 1

	path_to_file(path, upload_id)
	