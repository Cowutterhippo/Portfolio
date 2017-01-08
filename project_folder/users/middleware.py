class ajax( object ):
	def proces_request(self, request):
	request.context_dict = {
		'base_template': ' users/base.html'
	} 

	if request.is_ajax():
		request.context_dict['base_template'] = 'users/_ajax.html'