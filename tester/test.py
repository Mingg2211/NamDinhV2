import sys
sys.path.append('/home/admin/Desktop/bagsnlp/NamDinhV2/source')
from bot_brain import bot_searching

dki_kh = {"thủ tục đăng ký kết hôn" : ["Tối muốn đăng ký kết hôn", "Thủ tục cấp giấy xác nhận tình trạng hôn nhân", "Tôi muốn cưới thi cần nhưng thủ tục gì.", "Muốn kết hôn cần chuẩn bị những giấy tờ gì?", "Các bước đăng ký kết hôn với người nước ngoài", "Đăng ký lại kết hôn thực hiện như thế nào", "Hồ sơ đăng ký kết hôn gồm những gì? ", "Những giấy tờ gì phải trình khi đăng kí kết hôn?", "Để đăng ký kết hôn cần những điều kiện gì?", "Đơn vị nào sẽ tiếp nhận hồ sơ kết hôn?", "Đăng ký kết hôn có mất phí không?", "Tôi muốn lây chồng nước ngoài thi thủ túc kết hôn thế nào.", "Thủ tục đăng ký kết hôn với người nước ngoài bao lâu thi xong."]}
khaisinh = {"thủ tục đăng ký khai sinh":["Đăng ký khai sinh cho người đã có hồ sơ, giấy tờ cá nhân", "Cách để thực hiện làm giấy khai sinh cho con ", "Làm sao để làm giấy khai sinh cho con ", "Khai sinh cho con cần nhưng giấy tờ gì", "Hồ sơ đăng kí lại khai sinh gồm những giấy tờ gì?", "Đăng ký lại khai sinh yêu cầu điều kiện gì không?", "Đơn vị nào tiếp nhận hồ sơ đăng kí khai sinh?", "Chuẩn bị xong hồ sơ khai sinh phải nộp ở đâu?", "Đăng kí khai sinh có yếu tố nước ngoài cần xuất trình những giấy tờ gì?", "Người đã có hồ sơ, giấy tờ cá nhân có thể đăng kí lại khai sinh không?", "Tôi và ban gái chưa đăng ký kết hôn, thi thủ tục khai sinh cho con tôi  cần có những giấy tờ gì.", "Không có hộ khẩu có được đăng ký khai sinh không?", "Con sinh ở nước ngoiaf, có được đăng ký khai sinh ở việt nam không?", "Có bắt buộc phải có giấy chứng sinh mới được đăng ký khai sinh?"]}
khaitu = {"thủ tục đăng ký khai tử":["Hồ sơ đăng ký khai tử?", "Đơn vị tiếp nhận hồ sơ khai tử?", "Nộp hồ sơ khai tử ở đâu?", "Các bước đăng ký khai tử?", "Giải quyết yêu cầu đăng ký khai tử trong bao lâu?", "Đăng ký khai tử mất phí không?", "Các cách nộp hồ sơ khai tử?", "Đăng ký khai tử lưu động cần xuất trình giấy tờ gì?", "Điều kiện đăng ký khai tử lưu động?", "Làm thế nào để đăng ký lại khai tử?", "Bà tôi mât, tôi muốn đăng ký khai tử thi phải chuẩn bị những giấy tờ nào và thực hiện như thế nào", "Thủ tục đăng ký khai tử có yếu tố nước ngoài ", "Ai có trách nhiệm phải đăng ký khải tử? thời hạn bao lâu?", "Thủ tục đăng ký khai tử cho công dân việt nam hiện nay ra sao?", "Có thể đăng ký khai tử cho người chết đã lâu không có giấy báo tử không."]}
lyhon = {"thủ tục ghi vào sổ hộ tịch việc ly hôn, hủy việc kết hôn của công dân việt nam đã được giải quyết tại cơ quan có thẩm quyền của nước ngoài":["Ly hôn cần đến đâu?", "Viết đơn ly hôn có chữ ký hai vợ chồng rồi thủ tục ly hôn mất bao lâu?", "Hồ sơ cần chuẩn bị để ly hôn?", "Ly hôn cần điều kiện gì?", "Đơn vị nào tiếp nhận yêu cầu ly hôn?", "Các thủ tục ly hôn?", "Thủ tục li hôn kéo dài trong bao lâu thi xong. ", "Đơn phương lý hôn nhanh cần nhưng giấy tờ  gì ", "Những giầy tờ thủ tục cần thiết để li hôn với người nước ngoài ", "Đã nhập hộ khẩu về bên chông mà chồng không giao hộ khẩu có thực hiện thủ tục ly hôn được không?", "Nếu muốn lý hôn đơn phương nhưng giấy đăng ký kết hôn bị bên kia giữ có lý hôn được không", "Khi nộp hồ sơ li  hôn có được nộp bản sao giấy đăng ký kết hôn không", "Khi li hôn đơn phương có được nuôi con không?", "Thơi gian lý hôn đơn phương, thuận tình là bao lâu?", "Ly hôn mất bao nhiêu tiền", "Thuận tình li hôn là gì", "Không lên tòa có giải quyết  được li hôn không"]}
# datdai = {"":["Các loại thủ tục đất đai", "Làm thế nào để đăng ký đất đai lần đầu?", "Hồ sơ đăng ký đất đai gồm những gì?", "Cơ quan nào tiếp nhận hồ sơ đăng ký đất đai?", "Chuẩn bị xong hồ sơ đăng ký đất đai rồi nộp ở đâu?", "Thời hạn giải quyết yêu cầu đăng ký đất đai?", "Các mẫu đơn, tờ khai của thủ tục đăng ký đất đai?", "Giải quyết tranh chấp đất đai ở đâu?", "Đăng ký biến động quyền sử dụng đất", "Cơ quan giải quyết tranh chấp đất đai", "Nguyên tắc cấp giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất.", "Đất nông nghiệp nằm trong quy hoạch có được chuyển đổi thành mụch đích sử dụng đất không",]}
# khambenh = {"":["Đi khám bệnh cần các giấy tờ gì", "Đi khám bệnh có cần các giấy tờ ngay lập tức không?", "Tôi muốn chuyển tuyến để khám chữa bệnh cần giấy tờ gì không", "Các bước khám chữa bệnh bảo hiểm y tế?", "Các giấy tờ cần chuẩn bị khám chữa bệnh bảo hiểm y tế?", "Quy trình khám bệnh gồm những gì.?", "Chế độ hưởn g bảo hiểm  ý tế khi khám chữa bệnh trái tuyến", "Mức hưởng bảo hiểm ý tế với trường hợp khám chữa bệnh trái tuyến"]}
atlaodong = {"khai báo với sở lao động – thương binh và xã hội địa phương khi đưa vào sử dụng các loại máy, thiết bị, vật tư có yêu cầu nghiêm ngặt về an toàn lao động":["Các thủ tục an toàn lao động?", "Cơ quan nào tiếp nhận các thủ tục an toàn lao động?", "Muốn làm thủ tục an toàn lao động cần đến đâu"]}
baohiemthatnghiep = {"thủ tục giải quyết hưởng trợ cấp thất nghiệp":["Thủ tục hưởng trợ cấp thất nghiệp","Thủ tục chuyển nơi trợ cấp thất nghiệp","Được hưởng bảo hiểm thất nghiệp cần làm gì","Những người được hưởng bảo hiểm thất nghiệp ","Chế độ hưởng bảo hiểm thất nghiệp do đại dịch covid ảnh hưởng","Người đang hưởng trợ cấp thất nghiệp có được hưởng chế dộ bảo hiểm ý tế không","Lao động ngoài 60 tuổi có phải đóng bảo hiểm thất nghiêp không","Căn cứ vào đâu tính thời gian hưởng trợ cấp thất nghiệp","Quyền của người sử dụng lao động tham gia bảo hiểm thất nghiệp.","Thời gian nộp hồ sơ hưởng trợ cấp thất nghiệp trong bao lâu.","Tôi đã nghỉ việc rồi thì nhận tiền hỗ trợ thất nghiệp bằng cách nào.?,"]}
dichuc = {"thủ tục chứng thực di chúc":["Các thủ tục di chúc?", "làm thế nào để chứng thực di chúc?", "Thủ tục chứng thực di chúc do cơ quan nào thực hiện?", "Các giấy tờ cần để chứng thực di chúc?", "Chi phí làm thủ tục chứng thực di chúc?", "Nộp giấy tờ để chứng thực di chúc ở đâu?"]}


test_set = {"thủ tục đăng ký kết hôn" : ["Tối muốn đăng ký kết hôn", "Thủ tục cấp giấy xác nhận tình trạng hôn nhân", "Tôi muốn cưới thi cần nhưng thủ tục gì.", "Muốn kết hôn cần chuẩn bị những giấy tờ gì?", "Các bước đăng ký kết hôn với người nước ngoài", "Đăng ký lại kết hôn thực hiện như thế nào", "Hồ sơ đăng ký kết hôn gồm những gì? ", "Những giấy tờ gì phải trình khi đăng kí kết hôn?", "Để đăng ký kết hôn cần những điều kiện gì?", "Đơn vị nào sẽ tiếp nhận hồ sơ kết hôn?", "Đăng ký kết hôn có mất phí không?", "Tôi muốn lây chồng nước ngoài thi thủ túc kết hôn thế nào.", "Thủ tục đăng ký kết hôn với người nước ngoài bao lâu thi xong."],"thủ tục đăng ký khai sinh":["Đăng ký khai sinh cho người đã có hồ sơ, giấy tờ cá nhân", "Cách để thực hiện làm giấy khai sinh cho con ", "Làm sao để làm giấy khai sinh cho con ", "Khai sinh cho con cần nhưng giấy tờ gì", "Hồ sơ đăng kí lại khai sinh gồm những giấy tờ gì?", "Đăng ký lại khai sinh yêu cầu điều kiện gì không?", "Đơn vị nào tiếp nhận hồ sơ đăng kí khai sinh?", "Chuẩn bị xong hồ sơ khai sinh phải nộp ở đâu?", "Đăng kí khai sinh có yếu tố nước ngoài cần xuất trình những giấy tờ gì?", "Người đã có hồ sơ, giấy tờ cá nhân có thể đăng kí lại khai sinh không?", "Tôi và ban gái chưa đăng ký kết hôn, thi thủ tục khai sinh cho con tôi  cần có những giấy tờ gì.", "Không có hộ khẩu có được đăng ký khai sinh không?", "Con sinh ở nước ngoiaf, có được đăng ký khai sinh ở việt nam không?", "Có bắt buộc phải có giấy chứng sinh mới được đăng ký khai sinh?"],"thủ tục đăng ký khai tử":["Hồ sơ đăng ký khai tử?", "Đơn vị tiếp nhận hồ sơ khai tử?", "Nộp hồ sơ khai tử ở đâu?", "Các bước đăng ký khai tử?", "Giải quyết yêu cầu đăng ký khai tử trong bao lâu?", "Đăng ký khai tử mất phí không?", "Các cách nộp hồ sơ khai tử?", "Đăng ký khai tử lưu động cần xuất trình giấy tờ gì?", "Điều kiện đăng ký khai tử lưu động?", "Làm thế nào để đăng ký lại khai tử?", "Bà tôi mât, tôi muốn đăng ký khai tử thi phải chuẩn bị những giấy tờ nào và thực hiện như thế nào", "Thủ tục đăng ký khai tử có yếu tố nước ngoài ", "Ai có trách nhiệm phải đăng ký khải tử? thời hạn bao lâu?", "Thủ tục đăng ký khai tử cho công dân việt nam hiện nay ra sao?", "Có thể đăng ký khai tử cho người chết đã lâu không có giấy báo tử không."],"thủ tục ghi vào sổ hộ tịch việc ly hôn, hủy việc kết hôn của công dân việt nam đã được giải quyết tại cơ quan có thẩm quyền của nước ngoài":["Ly hôn cần đến đâu?", "Viết đơn ly hôn có chữ ký hai vợ chồng rồi thủ tục ly hôn mất bao lâu?", "Hồ sơ cần chuẩn bị để ly hôn?", "Ly hôn cần điều kiện gì?", "Đơn vị nào tiếp nhận yêu cầu ly hôn?", "Các thủ tục ly hôn?", "Thủ tục li hôn kéo dài trong bao lâu thi xong. ", "Đơn phương lý hôn nhanh cần nhưng giấy tờ  gì ", "Những giầy tờ thủ tục cần thiết để li hôn với người nước ngoài ", "Đã nhập hộ khẩu về bên chông mà chồng không giao hộ khẩu có thực hiện thủ tục ly hôn được không?", "Nếu muốn lý hôn đơn phương nhưng giấy đăng ký kết hôn bị bên kia giữ có lý hôn được không", "Khi nộp hồ sơ li  hôn có được nộp bản sao giấy đăng ký kết hôn không", "Khi li hôn đơn phương có được nuôi con không?", "Thơi gian lý hôn đơn phương, thuận tình là bao lâu?", "Ly hôn mất bao nhiêu tiền", "Thuận tình li hôn là gì", "Không lên tòa có giải quyết  được li hôn không"],"khai báo với sở lao động – thương binh và xã hội địa phương khi đưa vào sử dụng các loại máy, thiết bị, vật tư có yêu cầu nghiêm ngặt về an toàn lao động":["Các thủ tục an toàn lao động?", "Cơ quan nào tiếp nhận các thủ tục an toàn lao động?", "Muốn làm thủ tục an toàn lao động cần đến đâu"],"thủ tục giải quyết hưởng trợ cấp thất nghiệp":["Thủ tục hưởng trợ cấp thất nghiệp","Thủ tục chuyển nơi trợ cấp thất nghiệp","Được hưởng bảo hiểm thất nghiệp cần làm gì","Những người được hưởng bảo hiểm thất nghiệp ","Chế độ hưởng bảo hiểm thất nghiệp do đại dịch covid ảnh hưởng","Người đang hưởng trợ cấp thất nghiệp có được hưởng chế dộ bảo hiểm ý tế không","Lao động ngoài 60 tuổi có phải đóng bảo hiểm thất nghiêp không","Căn cứ vào đâu tính thời gian hưởng trợ cấp thất nghiệp","Quyền của người sử dụng lao động tham gia bảo hiểm thất nghiệp.","Thời gian nộp hồ sơ hưởng trợ cấp thất nghiệp trong bao lâu.","Tôi đã nghỉ việc rồi thì nhận tiền hỗ trợ thất nghiệp bằng cách nào.?,"],"thủ tục chứng thực di chúc":["Các thủ tục di chúc?", "làm thế nào để chứng thực di chúc?", "Thủ tục chứng thực di chúc do cơ quan nào thực hiện?", "Các giấy tờ cần để chứng thực di chúc?", "Chi phí làm thủ tục chứng thực di chúc?", "Nộp giấy tờ để chứng thực di chúc ở đâu?"]}

# print(test_set.keys())
# print(test_set.values())

print(test_set.items()[0])

# for item in dki_kh.items():
#     for value in item.values():
#         results = bot_searching(value.lower().replace('thủ tục',''))
#         if item.keys() in results:
#             print('dasd')
        