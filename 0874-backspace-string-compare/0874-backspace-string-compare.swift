class Solution {
    func backspaceCompare(_ s: String, _ t: String) -> Bool {
        return edited(s) == edited(t)
    }

    func edited(_ text: String) -> [String] {
        var editedText: [String] = []

        for letter in text {
            if letter == "#" && editedText != [] {
                editedText.popLast()
            }
            else if letter != "#" {
                editedText.append(String(letter))
            }
        }

        return editedText
    }
}