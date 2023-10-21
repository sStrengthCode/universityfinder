
var langCount = 0;
var sciCount = 0;
var mathCount = 0;
var otherCount = 0;

function toggleRadioButtons(checkbox)
{
    var radioButtons = checkbox.parentElement.querySelectorAll('input[type="radio"]');
    var sciences = document.querySelectorAll(".sciencesub");

    for (var i = 0; i < radioButtons.length; i++)
    {
        radioButtons[i].disabled = !checkbox.checked;
    }
    if (stream === "science")
    {
        if (checkbox.className === 'sciencesub')
        {
            radioButtons[0].checked = true;
            radioButtons[0].disabled = true;
            radioButtons[1].disabled = true;
        }
    }
    else if (stream === "art")
    {
        if (checkbox.className === 'sciencesub')
        {
            radioButtons[1].checked = true;
            radioButtons[0].disabled = true;
            radioButtons[1].disabled = true;
        }
        if (checkbox.className === "other")
        {
            radioButtons[0].checked = true;
            radioButtons[0].disabled = true;
            radioButtons[1].disabled = true;
        }
    }

    if (checkbox.checked)
    {
        if (checkbox.className === "sciencesub")
        {
            sciCount++;
        }

        else if (checkbox.className === "language")
        {
            langCount++;
        }

        else if (checkbox.className === "math")
        {
            mathCount++;
        }

        else if (checkbox.className === "other")
        {
            otherCount++;
        }
    }
    else
    {
        if (checkbox.className === "sciencesub")
        {
            sciCount--;
        }

        else if (checkbox.className === "language")
        {
            langCount--;
        }

        else if (checkbox.className === "math")
        {
            mathCount--;
        }

        else if (checkbox.className === "other")
        {
            otherCount--;
        }
    }

    // Bug here. science count is being incremented twice
    remaining();

}

function remaining()
{
    const languages = document.querySelectorAll(".language");
    const sciencesubs = document.querySelectorAll(".sciencesub");
    const others = document.querySelectorAll(".other");
    const maths = document.querySelectorAll(".math");
    const science = document.getElementById("science");
    const art = document.getElementById("art");
    const output = document.getElementById("output");
    const arrs = [science, art, ...languages, ...sciencesubs, ...others, ...maths]
    let mathCount = 0;
    let sciencesubCount = 0;
    let languageCount = 0;
    let otherCount = 0;


    function updateMathCount()
    {
        mathCount = 0;
        maths.forEach(function (math)
        {
            if (math.checked)
            {
                mathCount++;
            }
        });
    }

    function updateScienceCount()
    {
        sciencesubCount = 0;
        sciencesubs.forEach(function (sciencesub)
        {
            if (sciencesub.checked)
            {
                sciencesubCount++;
            }
        });
    }

    function updateLanguageCount()
    {
        languageCount = 0;
        languages.forEach(function (language)
        {
            if (language.checked)
            {
                languageCount++;
            }
        });
    }

    languages.forEach(function (language)
    {
        language.addEventListener("change", function ()
        {
            if (language.checked)
            {
                languageCount++;
            }
            else
            {
                languageCount--;
            }
        });
        updateLanguageCount();
        setText();
    });

    function updateotherCount()
    {
        otherCount = 0;
        others.forEach(function (other)
        {
            if (other.checked)
            {
                otherCount++;
            }
        });
    }

    others.forEach(function (other)
    {
        other.addEventListener("change", function ()
        {
            if (other.checked)
            {
                otherCount++;
            }
            else
            {
                otherCount--;
            }
        });
        updateotherCount();
        setText();
    });

    maths.forEach(function (math)
    {
        math.addEventListener("change", function ()
        {
            if (math.checked)
            {
                mathCount++;
            }
            else
            {
                mathCount--;
            }
        });
        updateMathCount();
        setText();
    });

    sciencesubs.forEach(function (sciencesub)
    {
        sciencesub.addEventListener("change", function ()
        {
            if (sciencesub.checked)
            {
                sciencesubCount++;
            }
            else
            {
                sciencesubCount--;
            }
        });
        updateScienceCount();
        setText();
    });

}

function disablecheckbox(checkbox_)
{
    const checkbox = document.querySelector('input[name="extendedessay"]');
    if (checkbox)
    {
        checkbox.disabled = true;
        checkbox.checked = false;
        var radioButtons = checkbox.parentElement.querySelectorAll('input[type="radio"]');
        for (var i = 0; i < radioButtons.length; i++)
        {
            radioButtons[i].disabled = !checkbox.checked;
            radioButtons[i].checked = false;
        }
    }
}

function enablecheckbox(checkbox_)
{
    const checkbox = document.querySelector('input[name="extendedessay"]');
    if (checkbox)
    {
        checkbox.disabled = false;
    }
}

function setText()
{
    const science = document.getElementById("science");
    const art = document.getElementById("art");
    const diploma = document.querySelector('input[name="c3"][value="diploma"]');
    const course = document.querySelector('input[name="c3"][value="course"]');
    const english = document.querySelectorAll('input[name="english"]');
    const arabic = document.querySelectorAll('input[name="arabic"]');
    const extendedessay = document.querySelector('input[name="extendedessay"]');

    if (science.checked)
    {
        art.disabled = true;
        stream = "science";
    }
    else if (art.checked)
    {
        science.disabled = true;
        stream = "art";
    }
    else
    {
        science.disabled = false;
        art.disabled = false;
    }


    if (diploma.checked)
    {
        course.disabled = true;
    }

    else if (course.checked)
    {
        diploma.disabled = true;
        english[0].disabled = true;
        arabic[0].disabled = true;
        extendedessay.disabled = true;
    }

    //     arrs.forEach(function(arr) {
    //     arr.addEventListener("click", function() {
    //     if (science.checked) {
    //         output.innerHTML = `language subjects remaining: ${2 - languageCount}<br>`;
    //         output.innerHTML += `Science subjects remaining: ${2 - sciencesubCount}<br>`;
    //         output.innerHTML += `Math subjects remaining: ${1 - mathCount}<br>`;
    //         output.innerHTML += `Extracurricular subjects remaining: ${1 - otherCount}<br>`;
    //     }

    //     if (art.checked) {
    //         output.innerHTML = `language subjects remaining: ${2 - languageCount}<br>`;
    //         output.innerHTML += `Science subjects remaining: ${1 - sciencesubCount}<br>`;
    //         output.innerHTML += `Math subjects remaining: ${1 - mathCount}<br>`;
    //         output.innerHTML += `Extracurricular subjects remaining: ${2 - otherCount}<br>`;
    //     }
    //     });
    // });
    restrict();
}

function restrict()
{
    const english = document.querySelectorAll('input[name="english"]');
    const arabic = document.querySelectorAll('input[name="arabic"]');
    const sciencesubs = document.querySelectorAll(".sciencesub");
    const maths = document.querySelectorAll(".math");
    const others = document.querySelectorAll(".other");
    const extendedessay = document.querySelector('input[name="extendedessay"]');
    // set restrictions

    if (stream === "science")
    {
        langLimit = 2;
        sciLimit = 2;
        mathLimit = 1;
        otherLimit = 1;
    }
    else 
    {
        langLimit = 2;
        sciLimit = 1;
        mathLimit = 1;
        otherLimit = 2;
    }


    if (stream === 'science')
    {
        const engCount = english[0].checked + english[1].checked;
        const arabCount = arabic[0].checked + arabic[1].checked;
        if (engCount === 1)
        {
            if (english[0].checked)
            {
                english[1].disabled = true; 
                english[0].disabled = true;
                arabic[0].disabled = true;
            }

            if(english[1].checked)
            {
                english[0].disabled = true;
                english[1].disabled = true;
                arabic[1].disabled = true;
            }

        }

        if (arabCount === 1)
        {
            if (arabic[0].checked)
            {
                arabic[1].disabled = true; 
                arabic[0].disabled = true;
                english[0].disabled = true;
            }

            if(arabic[1].checked)
            {
                arabic[0].disabled = true;
                arabic[1].disabled = true;
                english[1].disabled = true;
            }

        }

        if (sciCount === 2)
        {
            sciencesubs.forEach(function (sciencesub)
            {
                sciencesub.disabled = true;
            });
        }

        if (mathCount === 1)
        {
            maths[1].disabled = true;
            maths[0].disabled = true;
        }

        if (otherCount === 1)
        {
            others.forEach(function (other)
            {
                other.disabled = true;
            });
        }
        if (extendedessay.checked)
        {
            extendedessay.disabled = true;
        }
    }

    else if (stream === 'art')
    {
        const engCount = english[0].checked + english[1].checked;
        const arabCount = arabic[0].checked + arabic[1].checked;
        if (engCount === 1)
        {
            if (english[0].checked)
            {
                english[1].disabled = true;
                english[0].disabled = true;
            }

        }

        if (arabCount === 1)
        {
            if (arabic[0].checked)
            {
                arabic[1].disabled = true;
                arabic[0].disabled = true;
            }

        }

        if (sciCount === 1)
        {
            sciencesubs.forEach(function (sciencesub)
            {
                sciencesub.disabled = true;
            });
        }

        if (mathCount === 1)
        {
            if (maths[0].checked)
            {
                maths[1].disabled = true; maths[0].disabled = true;
            }
        }

        if (otherCount === 2)
        {
            others.forEach(function (other)
            {
                other.disabled = true;
            });
        }
        if (extendedessay.checked)
        {
            extendedessay.disabled = true;
        }
    }
}
