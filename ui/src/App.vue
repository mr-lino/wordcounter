<script setup>
import axios from 'axios'

async function submitText(inputText) {
  const data = {
    input_text: inputText.textinput
  }
  var wordCount
  axios.post('http://127.0.0.1:8000/word-count', data)
    .then(function (response) {
      console.log(response.data.word_count)
      wordCount = response.data.word_count
      alert(`Word count: ${wordCount}`);

    })
    .catch(function (error) {
      console.log(error);
    });
}

</script>

<template>
  <div class="word-counter-form">
    <h1>Mr Lino's Word Counter</h1>
    <FormKit
      type="form"
      #default="{ value }"
      @submit="submitText"
      submit-label="Submit"

    >
      <FormKit
        type="textarea"
        name="textinput"
        label="Text Input"
        help="Please, input some text"
        validation="required"
      />      
      <!-- <pre>{{ value }}</pre> -->
    </FormKit>
  </div>
</template>

<style scoped>
.word-counter-form {
  width: calc(100% - 2em);
  max-width: 480px;
  box-sizing: border-box;
  padding: 2em;
  box-shadow: 0 0 1em rgba(0, 0, 0, .1);
  border-radius: .5em;
  margin: 4em auto;
}

.logo {
  width: 150px;
  height: auto;
  display: block;
  margin: 0 auto 2em auto;
}
pre {
  background-color: rgba(0, 100, 250, .1);
  padding: 1em;
}
h1 {
  font-family:  Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  font-size: 2.0em;
  line-height: 1.1;
}
</style>
