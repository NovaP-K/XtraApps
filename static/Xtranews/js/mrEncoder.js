function encoderOfTheTitle(originalText) {

    var double_quote_out = originalText.replace(/"/g, "$22$") ;
    var single_quote_out = double_quote_out.replace(/'/g, "$27$");
    var question_mark_out = single_quote_out.replace(/\?/g, "$3F$");
    var hash_tag_out = question_mark_out.replace(/\#/g, "$23$");
    var hyphen_out = hash_tag_out.replace(/\-/g, "$hyphen$");
    var space_out = hyphen_out.replace(/\ /g, '-');

    var encodedText = space_out ;
    return encodedText;
}
