# Validation Workflow Rules - ALWAYS FOLLOW

## 🚨 **CRITICAL REQUIREMENTS**

### **NEVER Make Unverified Claims**

- ❌ **DO NOT** say "✅ Fixed" without visual confirmation
- ❌ **DO NOT** claim "✅ Working" without testing
- ❌ **DO NOT** assume CSS changes work without validation

### **ALWAYS Follow This Workflow**

#### **1. Build & Deploy Phase**

```bash
# Always rebuild after CSS changes
npm run build

# Restart development server
pkill -f docusaurus && sleep 2 && npm run start

# Wait for server to be ready
sleep 15 && curl -s -o /dev/null -w "%{http_code}" http://localhost:3000
```

#### **2. Visual Validation Phase**

- **REQUIRED**: Open browser and visually inspect the page
- **REQUIRED**: Test responsive behavior by resizing viewport
- **REQUIRED**: Verify each specific issue is resolved
- **REQUIRED**: Check for new issues introduced

#### **3. CSS Verification Phase**

```bash
# Verify CSS is compiled
curl -s http://localhost:3000/styles.css | grep -A 5 "specific-rule-name"

# Check for conflicting rules
curl -s http://localhost:3000/styles.css | grep -A 3 -B 3 "display: none"
```

#### **4. Documentation Phase**

- **REQUIRED**: List actual visual problems found
- **REQUIRED**: Document what was fixed vs. what remains
- **REQUIRED**: Note any new issues introduced
- **REQUIRED**: Provide evidence of fixes (screenshots, CSS output)

## 📋 **Validation Checklist Template**

### **Before Claiming "Fixed"**

- [ ] **Build completed** without errors
- [ ] **Server restarted** and running
- [ ] **Browser opened** and page loaded
- [ ] **Visual inspection** completed
- [ ] **Responsive testing** completed
- [ ] **Specific issues** verified resolved
- [ ] **No new issues** introduced
- [ ] **CSS rules** confirmed working

### **Evidence Required**

- Screenshots showing before/after
- CSS compilation verification
- Browser developer tools inspection
- Responsive viewport testing

## 🎯 **Problem-Solving Workflow**

### **1. Identify Visual Problems**

- List specific, observable issues
- Take screenshots for reference
- Note viewport dimensions

### **2. Implement Incremental Fixes**

- Make ONE change at a time
- Rebuild and test after EACH change
- Verify fix before moving to next issue

### **3. Validate Each Fix**

- Confirm specific problem resolved
- Check no new problems introduced
- Test across different viewport sizes

### **4. Document Results**

- What was fixed
- What remains broken
- Evidence of improvements
- Any regressions

## 🚫 **Prohibited Statements**

### **NEVER Say These Without Validation**

- "✅ Fixed" - unless visually confirmed
- "✅ Working" - unless tested
- "✅ Responsive" - unless verified across viewports
- "✅ No conflicts" - unless CSS verified
- "✅ Complete" - unless all issues resolved

### **ALWAYS Say These Instead**

- "🔍 Investigating issue..."
- "🧪 Testing fix..."
- "📸 Verifying visually..."
- "⚠️ Issue remains, need further investigation"
- "✅ Confirmed fixed with evidence: [screenshot/CSS]"

## 🔄 **Continuous Validation**

### **After Each Change**

1. **Build** the project
2. **Restart** the server
3. **Open** browser
4. **Inspect** visually
5. **Test** responsive behavior
6. **Document** results
7. **Repeat** if issues remain

### **Final Validation**

- All original issues resolved
- No new issues introduced
- Responsive behavior working
- CSS properly compiled
- Visual appearance correct

---

**Priority**: This workflow takes precedence over all other rules
**Enforcement**: Must be followed for every development task
**Validation**: Claims of success require visual evidence
**Documentation**: All results must be documented with evidence
