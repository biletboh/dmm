var callbackForm = {
  template: " <div class='col-sm-6 col-sm-offset-3 sm-margin-b-30'> <form id='callbackForm'> <input type='text' class='form-control footer-input margin-b-20' placeholder='Name' required> <input type='email' class='form-control footer-input margin-b-20' placeholder='Email' required> <input type='text' class='form-control footer-input margin-b-20' placeholder='Phone' required> <textarea class='form-control footer-input margin-b-30' rows='6' placeholder='Message' required></textarea> <button type='submit' class='btn-theme btn-theme-sm btn-base-bg text-uppercase'>Submit</button> </form> </div>"
};

new Vue({
  el: '#tests-block',
  data: {
    position: 0,
    startTestButton: true,
    showTest: false,
    showForm: true,
    testResult: false,
    titles: [
      'In which industry do you work / plan to work?',
      'What is your experience in this industry?',
      'What is the main task at this stage of your work?',
      'How can you describe the work of your project at this stage?',
      'Choose the most accurate option that characterizes your project',
      'What is the current / planned coverage of your project?',
      'Do you have a call center?',
      'Is there a marketing department in your company/is it planned in near future?',
      'What is the most convenient way for you to accept payments for services provision?',
      'What is the indicator that shows the state of overbought or oversold market?'
    ],
    questions: [
      ['Forex', 'Binary', 'ICO', 'Cloud Mining', 'Online Games', 'Other'],
      ['Up to 1 year', 'From 1 to 3 years', 'More than 3 years', 'I want to found a startup and I don’t have experience'],
      ['Create a new turn-key project from scratch ', 'Create a general marketing strategy for my project', 'Connect the optimal payment system for my project', 'Increase the number of leads for my project', 'Strengthen brand by increasing audience coverage', 'Other'],
      ['I have not done a great job of it so far', 'I passed the preparatory stage and I plan to start active attracting clients', 'All necessary directions of my business are created and started', 'Everything works perfectly, but I want a point improvement of some processes', 'Other'],
      ['The development strategy is strong and was adjusted a minimum number of times', 'I have no strategy, I act through the way of trial and error', 'The main activity is considered to the detail but at some points I don’t have the right planning', 'In my opinion, my approach is situational. It is extremely difficult to build a long-term strategy of actions', 'Other'],
      ['Small group in one of the countries', 'Broad coverage in one country', 'Limited audience in several countries', 'Large audience in several countries', 'Other'],
      ['I have/plan to create my own call center', 'I use / plan to use outsourced call center', 'I replace the call center with messaging or chatting', 'The process of communication with customers is robotized', 'I don’t see the need to create a call center', 'Other'],
      ['Yes, we develop/plan to develop all the necessary creatives ourselves', 'No, we order advertisement at advertising agencies or freelancers', 'We plan our activity for a long-term and order all advertising support on a contract basis, following the brand-book and the general strategy', 'Other'],
      ['Bank cards', 'Bank Transfer', 'E-Wallet', 'Cryptocurrency', 'Other']
    ]
  },
	methods: {
		nextQuestion: function() {
			$('input[type=radio]').each(function(){
							this.checked = false;
			});
			if(this.position < 8) {
				this.position++;
			} else {
        this.startTestButton = false;
        this.showTest = false;
				this.testResult = true;
        this.showForm = true;
			}

		}
	},
  components: {
    'callback-form': callbackForm
  }
})


