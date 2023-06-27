function calculate_modifier(attributeValue) {
    return Math.floor((attributeValue - 10) / 2);
}
function updateModifier(attribute) {
    let modifierInput = document.getElementById('val-' + attribute);
    let disabledInput = document.getElementById('mod-' + attribute);
    // Calcula el nuevo valor del atributo según la función "calculate_modifier"
    let updatedValue = calculate_modifier(modifierInput.value);
    disabledInput.value = updatedValue;
}