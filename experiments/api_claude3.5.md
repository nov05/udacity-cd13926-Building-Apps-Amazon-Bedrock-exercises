

* Claude 3.5 Sonnet By: Anthropic

  * https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/model-catalog/serverless/anthropic.claude-3-5-sonnet-20240620-v1:0

  * API payload:  
    ```json
    {
      "modelId": "anthropic.claude-3-5-sonnet-20240620-v1:0",
      "contentType": "application/json",
      "accept": "application/json",
      "body": {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "image",
                "source": {
                  "type": "base64",
                  "media_type": "image/jpeg",
                  "data": "iVBORw..."
                }
              },
              {
                "type": "text",
                "text": "What's in this image?"
              }
            ]
          }
        ]
      }
    }
    ```

  * AWS CLI
    ```bash
    aws bedrock-runtime invoke-model \
    --model-id anthropic.claude-3-sonnet-20240229-v1:0 \
    --body '{"anthropic_version": "bedrock-2023-05-31", "max_tokens": 1000, "messages": [{"role": "user", "content": "What is the capital of Frnace?"}]}' \
    --cli-binary-format raw-in-base64-out \
    output.json
    ```

  * AWS CLI: Conversational call
    ```bash
    aws bedrock-runtime invoke-model \
    --model-id anthropic.claude-3-sonnet-20240229-v1:0 \
    --body '{"anthropic_version": "bedrock-2023-05-31", "max_tokens": 1000, "messages": [
        {"role": "user", "content": "Give me recipe to bake chocolate cookies"},
        {"role": "assistant", "content": "Here is a recipe for delicious homemade chocolate cookies:\n\nChocolate Cookies\n\nIngredients:\n- 1 1/4 cups (220g) all-purpose flour\n- 3/4 cup (65g) cocoa powder\n- 1 tsp baking soda\n- 1/2 tsp salt\n- 1 cup (180g) semi-sweet chocolate chips\n- 1 cup (230g) unsalted butter, softened\n- 1 1/4 cups (250g) granulated sugar\n- 2 large eggs\n- 1 tsp vanilla extract\n\nInstructions:\n1. Preheat oven to 375°F (190°C). Line two baking sheets with parchment paper.\n2. In a large bowl, beat the butter and sugar together until light and fluffy, about 2-3 minutes. Beat in the eggs one at a time, then stir in the vanilla.\n3. In a separate bowl, whisk together the flour, cocoa powder, baking soda, and salt.\n4. Gradually mix the dry ingredients into the wet ingredients until just combined. Fold in the chocolate chips.\n5. Scoop dough by rounded tablespoonfuls onto the prepared baking sheets, spacing them about 2 inches apart.\n6. Bake for 8-10 minutes, until the edges are set but the centers are still soft.\n7. Allow cookies to cool on the sheet for 5 minutes before transferring to a wire rack to cool completely.\n\nMakes about 24 cookies. Enjoy with a glass of cold milk or scoop of ice cream!"},
        {"role": "user", "content": "How many cookies does this recipe make?"}
    ]}' \
    --cli-binary-format raw-in-base64-out \
    output.json
    ```

* Verify AWS config (Powershell)

```
aws configure list
Notepad ~/.aws/credentials 
aws bedrock list-foundation-models
```

* Query the model  

```
aws bedrock invoke-model `
--model-id anthropic.claude-3-5-sonnet-20240620-v1:0 `
--body claude_input.json output.json
```
  